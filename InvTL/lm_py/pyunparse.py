
#!/usr/local/bin/python

# Copyright (c) 2005 Andrew R. Gross <andy@andygross.org>
#   Modified by Michael Gorbovitski
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to 
# deal in the Software without restriction, including without limitation the 
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or 
# sell copies of the Software, and to permit persons to whom the Software is 
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in 
# all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL 
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING 
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER 
# DEALINGS IN THE SOFTWARE.


__author__  = 'Andrew Gross <andy@andygross.org>, mickg@mickg.net'
__version__ = (0,3)

import sys
from compiler.visitor import ASTVisitor
from compiler import parse, walk
from compiler.consts import *
from optparse import OptionParser

class UnparsingVisitor(ASTVisitor): 
    def __init__(self, stream=None):
        if stream is None:
            self.stream = sys.stdout
        else:
            self.stream = stream
        self.indents = 0
        self.v = lambda tree, visitor=self: walk(tree, visitor)
        ASTVisitor.__init__(self)

    def DEDENT(self):
        self.indents -=1
        self.NEWLINE()
            
    def INDENT(self):
        self.indents += 1
        self.NEWLINE()

    def NEWLINE(self):
        self.stream.write('\n')
        self.stream.write(' ' * 4 * self.indents )
        
    def write(self, data):
        self.stream.write(data)

    def visitBlock(self, block):
        self.INDENT()
        self.v(block)
        self.DEDENT()

    def visitAdd(self, node):
        self.write("(")
        self.v(node.left)
        self.write(" + ")
        self.v(node.right)
        self.write(")")

    def visitAnd(self, node):
        self.write("(")
        for i in range(len(node.nodes)):
            self.v(node.nodes[i])
            if i < (len(node.nodes) - 1):
                self.write(" and ")
        self.write(")")

    def visitAssAttr(self, node):
        node.flags == OP_DELETE and self.write("del ")
        self.v(node.expr, self)
        self.write(".%s" % node.attrname)
        node.flags == OP_DELETE and self.NEWLINE()

    def visitAssList(self, node):
        self.write("[")
        for i in (self.v(n, self) for n in node.nodes):
            self.write(",")
        self.write("]")

    def visitAssName(self, node):
        node.flags == OP_DELETE and self.write("del ")
        self.write(node.name)
        node.flags == OP_DELETE and self.NEWLINE()
        
    def visitAssTuple(self, node):
        #print dir(node.nodes[0])
        if 'flags' in dir(node.nodes[0]) and node.nodes[0].flags == OP_DELETE:
            for n in node.nodes: self.v(n)
        else:
            self.write("(")
            for i in (self.v(n) for n in node.nodes):
                self.write(",")
            self.write(")")

    def visitAssert(self, node):
        self.write('assert ')
        self.v(node.test)
        if node.fail:
            self.write(", ")
            self.v(node.fail)
        self.NEWLINE()

    def visitAssign(self, node):
        for i in range(len(node.nodes)):
            n = node.nodes[i]
            self.v(n)
            if i < len(node.nodes):
                self.write(" = ")
        self.v(node.expr)
        self.write(" ")
        self.NEWLINE()

    def visitAugAssign(self, node):
        self.v(node.node)
        self.write(" %s " % node.op)
        #print "AUGASSIG: ",node.expr 
        if "value" in dir(node.expr):
            self.write(repr(node.expr.value))
        else:
            self.v(node.expr)
        self.NEWLINE()
        #assert False

    def visitBackquote(self, node):
        self.write("`")
        self.v(node.expr)
        self.write("`")

    def visitBitand(self, node):
        self.write("(")
        for i in range(len(node.nodes)):
            self.v(node.nodes[i])
            if i < (len(node.nodes) - 1):
                self.write(" & ")
        self.write(")")

    def visitBitor(self, node):
        self.write("(")
        for i in range(len(node.nodes)):
            self.v(node.nodes[i])
            if i < (len(node.nodes) - 1):
                self.write(" | ")
        self.write(")")

    def visitBitxor(self, node):
        self.write("(")
        for i in range(len(node.nodes)):
            self.v(node.nodes[i])
            if i < (len(node.nodes) - 1):
                self.write(" ^ ")        
        self.write(")")

    def visitBreak(self, node):
        self.write("break ")
        self.NEWLINE()
        
    def visitCallFunc(self, node):
        self.v(node.node)
        self.write("(")
        for i in range(len(node.args)):
            self.v(node.args[i])
            if i < (len(node.args) - 1):
                self.write(", ")
        if node.star_args:
            if len(node.args):
                self.write(", ")
            self.write("*")
            self.v(node.star_args)
        if node.dstar_args:
            if node.args or node.star_args:
                self.write(", ")
            self.write("**")
            self.v(node.dstar_args)
        self.write(")")
        
    def visitClass(self, node):
        self.write("class %s" % node.name)
        if node.bases: self.write("(")
        else: self.write(":")
        for i in range(len(node.bases)):
            self.v(node.bases[i])
            if i < len(node.bases) - 1:
                self.write(",")
            else:
                self.write("):")
        self.INDENT()
        self.v(node.code)
        self.DEDENT()
        
    def visitCompare(self, node):
        self.v(node.expr)
        for operator, operand in node.ops:
            self.write(" %s " % operator)
            self.v(operand)

    def visitConst(self, node):
        #print "CONST: ",node.value
        self.write(repr(node.value))

    def visitContinue(self, node):
        self.write("continue ")
        
    def visitDecorators(self, node):
        for n in node.nodes:
            self.write("@")
            self.v(n)

    def visitDict(self, node):
        self.write("{")
        for i in range(len(node.items)):
            k, v = node.items[i]
            self.v(k)
            self.write(" : ")
            self.v(v)
            if i < len(node.items) - 1:
                self.write(" , ")
        self.write("} ")

    def visitDiscard(self, node):
        self.v(node.expr)
        self.NEWLINE()

    def visitDiv(self, node):
        self.v(node.left)
        self.write(" / ")
        self.v(node.right)

    def visitFloorDiv(self, node):
        self.v(node.left)
        self.write(" // ")
        self.v(node.right)        

    def visitEllipsis(self, node):
        self.write(",...,")

    def visitExec(self, node):
        self.write("exec ")
        self.v(node.expr)
        if node.globals:
            self.write(" in ")
            self.v(node.globals)
        if node.locals:
            self.write(', ')
            self.v(node.locals)
        self.NEWLINE()
        
    def visitFor(self, node):
        self.write("for ")
        self.v(node.assign)
        self.write(" in ")
        self.v(node.list)
        self.write(":")
        self.INDENT()
        self.v(node.body)
        self.DEDENT()
        if node.else_:
            self.write("else:")
            self.INDENT()
            self.v(node.else_)
            self.DEDENT()

    def visitFrom(self, node):
        self.write("from %s import " % node.modname)
        for i in range(len(node.names)):
            name, alias = node.names[i]
            self.write(name)
            if alias:
                self.write(" as %s" % alias)
            if i < len(node.names) - 1:
                self.write(", ")
        self.NEWLINE()

    def visitFunction(self, node):
        if node.decorators:
            for d in node.decorators:
                self.write("@")
                self.v(d)
                self.NEWLINE()

        hasvar = haskw = hasone = hasboth = False

        ndefaults = len(node.defaults)

        if node.flags & CO_VARARGS:
            hasone = hasvar = True
        if node.flags & CO_VARKEYWORDS:
            hasone = haskw = True
        hasboth = hasvar and haskw

        kwarg = None
        vararg = None
        defargs = []
        newargs = node.argnames[:]


        if haskw:
            kwarg = "**%s" % newargs.pop()

        if hasvar:
            vararg = "*%s" % newargs.pop()
            
        if ndefaults:
            for i in range(ndefaults):
                defargs.append((newargs.pop(), node.defaults.pop()))
            defargs.reverse()
        
        self.write("def %s(" % node.name)
        for i in range(len(newargs)):
            if isinstance(newargs[i], tuple):
                self.write("(%s, %s)" % newargs[i])
            else:
                self.write(newargs[i])
            if i < len(newargs) - 1:
                self.write(", ")
        if defargs and len(newargs):
            self.write(", ")

        for i in range(len(defargs)):
            name, default = defargs[i]
            self.write("%s=" % name)
            self.v(default)
            if i < len(defargs) - 1:
                self.write(", ")
        
        if vararg:
            if (newargs or defargs):
                self.write(", ")
            self.write(vararg)
        if kwarg:
            if (newargs or defargs or vararg):
                self.write(", ")
            self.write(kwarg)

        self.write("):")
        self.INDENT()
        self.v(node.code)
        self.DEDENT()

    def visitGenExpr(self, node):
        self.write("(")
        self.v(node.code)
        self.write(")")

    def visitGenExprFor(self, node):
        self.write(" for ")
        self.v(node.assign)
        self.write(" in ")
        self.v(node.iter)
        for if_ in node.ifs:
            self.write(" if ")
            self.v(if_)

    def visitGetattr(self, node):
        self.v(node.expr)
        self.write(".%s" % node.attrname)

    def visitGlobal(self, node):
        for n in node.names:
            self.write("global %s" % n)
            self.NEWLINE()

    def visitIf(self, node):
        for c, b in node.tests:
            self.write("if ")
            self.v(c)
            self.write(':')
            self.INDENT()
            self.v(b)
            self.DEDENT()
        if node.else_:
            self.write("else:")
            self.INDENT()
            self.v(node.else_)
            self.DEDENT()
            
    def visitImport(self, node):
        self.write("import ")
        for i in range(len(node.names)):
            name, alias = node.names[i]
            self.write(name)
            if alias:
                self.write(" as %s" % alias)
            if i < len(node.names) - 1:
                self.write(", ")
                
        self.NEWLINE()

    def visitInvert(self, node):
        self.write("~")
        self.v(node.expr)

    def visitKeyword(self, node):
        self.write(node.name)
        self.write("=")
        self.v(node.expr)


    def visitLambda(self, node):
        hasvar = haskw = hasone = hasboth = False

        ndefaults = len(node.defaults)

        if node.flags & CO_VARARGS:
            hasone = hasvar = True
        if node.flags & CO_VARKEYWORDS:
            hasone = haskw = True
        hasboth = hasvar and haskw

        kwarg = None
        vararg = None
        defargs = []
        newargs = node.argnames[:]


        if haskw:
            kwarg = "**%s" % newargs.pop()

        if hasvar:
            vararg = "*%s" % newargs.pop()
            
        if ndefaults:
            for i in range(ndefaults):
                defargs.append((newargs.pop(), node.defaults.pop()))
            defargs.reverse()
        
        self.write("lambda ")
        for i in range(len(newargs)):
            if isinstance(newargs[i], tuple):
                self.write("(%s, %s)" % newargs[i])
            else:
                self.write(newargs[i])
            if i < len(newargs) - 1:
                self.write(", ")
        if defargs and len(newargs):
            self.write(", ")

        for i in range(len(defargs)):
            name, default = defargs[i]
            self.write("%s=" % name)
            self.v(default)
            if i < len(defargs) - 1:
                self.write(", ")
        
        if vararg:
            if (newargs or defargs):
                self.write(", ")
            self.write(vararg)
        if kwarg:
            if (newargs or defargs or vararg):
                self.write(", ")
            self.write(kwarg)
        self.write(" : ")
        self.v(node.code)


    def visitLeftShift(self, node):
        self.v(node.left)
        self.write(" << ")
        self.v(node.right)

    def visitList(self, node):
        self.write('[')
        for i in range(len(node.nodes)):
            self.v(node.nodes[i])
            if i < len(node.nodes) - 1:
                self.write(",")
        self.write("]")

    def visitListComp(self, node):
        self.write("[")
        self.v(node.expr)
        for qual in node.quals:
            self.write(" for ")
            self.v(qual)
        self.write("]")

    def visitListCompFor(self, node):
        self.v(node.assign)
        self.write(" in ")
        self.v(node.list)
        for if_ in node.ifs:
            self.v(if_)
            
    def visitListCompIf(self, node):
        self.write(" if ")
        self.v(node.test)

    def visitMod(self, node):
        self.v(node.left)
        self.write(" % ")
        self.v(node.right)

    def visitModule(self, node):
        #@if node.doc:
        # #   self.write(repr(node.doc))
        self.v(node.node)

    def visitMul(self, node):
        self.write("(")
        self.v(node.left)
        self.write(" * ")
        self.v(node.right)
        self.write(")")

    def visitName(self, node):
        self.write(node.name)

    def visitNot(self, node):
        self.write("(")
        self.write(" not ")
        self.v(node.expr)
        self.write(")")
        
    def visitOr(self, node):
        self.write("(")
        for i in range(len(node.nodes)):
            self.v(node.nodes[i])
            if i < len(node.nodes) - 1:
                self.write(" or ")
        self.write(")")

    def visitPass(self, node):
        self.write("pass ")

    def visitPower(self, node):
        self.v(node.left)
        self.write(" ** ")
        self.v(node.right)

    def visitPrint(self, node):
        self.write("print ")
        nnodes = len(node.nodes)
        for i in range(nnodes):
            n = node.nodes[i]
            self.v(n)
            if i < nnodes - 1:
                self.write(", ")
        if node.dest: self.write(" >> " ); self.v(node.dest)

    def visitPrintnl(self, node):
        self.write("print ")
        nnodes = len(node.nodes)
        for i in range(nnodes):
            n = node.nodes[i]
            self.v(n)
            if i < nnodes - 1:
                self.write(", ")
        if node.dest: self.write(" >> " ); self.v(node.dest)
        self.NEWLINE()

    def visitRaise(self, node):
        self.write("raise ")
        if node.expr1: self.v(node.expr1)
        if node.expr2: self.write(", "); self.v(node.expr2)
        if node.expr3: self.v(node.expr3)
        self.NEWLINE()
        
    def visitReturn(self, node):
        self.write("return ")
        self.v(node.value)

    def visitRightShift(self, node):
        self.write("(")
        self.v(node.left)
        self.write(" >> ")
        self.v(node.right)
        self.write(")")

    def visitSlice(self, node):
        node.flags == OP_DELETE and self.write("del ")
        self.v(node.expr)
        self.write("[")
        if node.lower:
            self.v(node.lower)
        self.write(":")
        if node.upper:
            self.v(node.upper)
        self.write("]")
        node.flags == OP_DELETE and self.NEWLINE()


    def visitStmt(self, node):
        for n in node.nodes:
            self.v(n)
        
    def visitSub(self, node):
        self.write("(")
        self.v(node.left)
        self.write(" - ")
        self.v(node.right)
        self.write(")")

    def visitSubscript(self, node):
        isdel = False
        if node.flags == OP_DELETE: isdel = True
        isdel and self.write("del ")
        self.v(node.expr)
        self.write("[")
        for i in range(len(node.subs)):
            self.v(node.subs[i])
            if i == len(node.subs) - 1:
                self.write("]")
        node.flags == OP_DELETE and self.NEWLINE()
        
    def visitTryExcept(self, node):
        self.write("try:")
        self.visitBlock(node.body)
        for h in node.handlers:
            self.write("except")
            expr, target, body = h
            if expr:
                self.write(" ")
                self.v(expr)
            if target:
                self.write(", ")
                self.v(target)
            self.write(":")
            self.visitBlock(body)
        if node.else_:
            self.write("else:")
            self.INDENT()
            self.v(node.else_)
            self.DEDENT()
        self.NEWLINE()
        
    def visitTryFinally(self, node):
        self.write("try:")
        self.INDENT()
        self.v(node.body)
        self.DEDENT()
        self.write("finally:")
        self.INDENT()
        self.v(node.final)
        self.DEDENT()

    def visitTuple(self, node):
        self.write('(')
        for i in range(len(node.nodes)):
            self.v(node.nodes[i])
            if i < len(node.nodes) - 1:
                self.write(",")
        self.write(")")

    def visitUnaryAdd(self, node):
        self.write("(")
        self.write("+")
        self.v(node.expr)
        self.write(")")

    def visitUnarySub(self, node):
        self.write("(")
        self.write("-")
        self.v(node.expr)
        self.write(")")

    def visitWhile(self, node):
        self.write("while ")
        self.v(node.test)
        self.write(":")
        self.INDENT()
        self.v(node.body)
        if node.else_:
            self.DEDENT()
            self.write("else:")
            self.INDENT()
            self.v(node.else_)
        self.DEDENT()
        
    def visitYield(self, node):
        self.write("yield ")
        self.v(node.value)
        self.NEWLINE()


def ast2py(ast, stream=None):
    if stream is None:
        stream = sys.stdout
    v = UnparsingVisitor(stream=stream)
    v.v(ast)


