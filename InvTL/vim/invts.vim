" Vim syntax file
" Language:	InvTS
" Maintainer:	Michael Gorbovitski <mickg@mickg.net>
"
" Options to control InvTS syntax highlighting:
"
" For version 5.x: Clear all syntax items
" For version 6.x: Quit when a syntax file was already loaded
" Put the following into your vimrc file
"   au BufNewFile,BufRead *.invtl			setf invts

if version < 600
  syntax clear
elseif exists("b:current_syntax")
  finish
endif
let c_no_curly_error=1
let python_highlight_all = 1
syn include @InvTSPython syntax/pythoninvts.vim 
unlet b:current_syntax
syn include @InvTSC syntax/cinvts.vim 
unlet b:current_syntax

syn keyword InvTSStatement	inv at  
syn match   InvTSStatement	"do" nextgroup=InvTSLanguageSpec
syn match   InvTSStatement	"do\s\+before" nextgroup=InvTSLanguageSpec
syn match   InvTSStatement	"do\s\+after" nextgroup=InvTSLanguageSpec
syn match   InvTSStatement	"do\s\+instead" nextgroup=InvTSLanguageSpec

syn keyword InvTSLanguageSpec   C nextgroup=InvTSSubjectCBody
syn keyword InvTSLanguageSpec   py nextgroup=InvTSSubjectPyBody

syn region  InvTSIf             start="if\s*("rs=e+1,ms=e+1 end=")"re=s-1,me=s-1 contains=@InvTSPython,InvTSCondition transparent
syn region  InvTSCondition      start="("hs=e+1 end=")"he=s-1 contains=@InvTSPython,InvTSCondition contained
"syn keyword InvTSStatement      if

"syn match   InvTSStatement       "de\s\+in\s\+file"
"syn match   InvTSStatement       "de\s\+in\s\+function"
"syn match   InvTSStatement       "de\s\+in\s\+class"
syn region  InvTSDeCondit 	start="de\s\+in\s\+file\s*("ms=e+1 end=")"me=s-1 contains=@InvTSPython,InvTSCondition 
syn region  InvTSDeCondit 	start="de\s\+in\s\+function\s*("ms=e+1 end=")"me=s-1 contains=@InvTSPython,InvTSCondition nextgroup=InvTSLanguageSpec
syn region  InvTSDeCondit 	start="de\s\+in\s\+class\s*("ms=e+1 end=")"me=s-1 contains=@InvTSPython,InvTSCondition nextgroup=InvTSLanguageSpec

syn region  InvTSSubjectCBody   start="{"hs=e+1 end="}"he=s-1 contains=@InvTSC,InvTSSubjectCBody containedin=InvTSLanguageSpec
syn region  InvTSSubjectPyBody  start="{"hs=e+1 end="}"he=s-1 contains=@InvTSPython,InvTSSubjectPyBody containedin=InvTSLanguageSpec

syn match   InvTSComment	"#.*$" 
" syn keyword InvTSStatement2      de file function if 



syn match   InvTSMeta           "\$[a-zA-Z_][a-zA-Z0-9_]*"

if exists("InvTS_highlight_all")
  let InvTS_highlight_numbers = 1
  let InvTS_highlight_builtins = 1
endif


" This is fast but code inside triple quoted strings screws it up. It
" is impossible to fix because the only way to know if you are inside a
" triple quoted string is to start from the beginning of the file. If
" you have a fast machine you can try uncommenting the "sync minlines"
" and commenting out the rest.
syn sync match InvTSSync grouphere NONE "):$"
syn sync maxlines=200
"syn sync minlines=2000

if version >= 508 || !exists("did_InvTS_syn_inits")
  if version <= 508
    let did_InvTS_syn_inits = 1
    command -nargs=+ HiLink hi link <args>
  else
    command -nargs=+ HiLink hi def link <args>
  endif

  " The default methods for highlighting.  Can be overridden later
  HiLink InvTSStatement	        Statement
  HiLink InvTSLanguageSpec      Define
  HiLink InvTSConditional	Conditional
  HiLink InvTSLocation          Statement
  HiLink InvTSLocation2         Special
"  HiLink InvTSString		String
"  HiLink InvTSRawString	String
  HiLink InvTSMeta		String
"  HiLink InvTSOperator		Operator
"  HiLink InvTSPreCondit	PreCondit
  HiLink InvTSComment		Comment
"  HiLink InvTSTodo		Todo
"  HiLink InvTSSubjectCBody      PreCondit
  delcommand HiLink
endif

let b:current_syntax = "invts"

" vim: ts=8
