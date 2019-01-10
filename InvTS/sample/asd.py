inv $r = py{len($s)} if (isVar($s))
(
    at py{$s = set()}
    do after py{
        $r = 0
    }
    at py{$s.add($x)}
    do before py{
        if $x not in $s:
            $r += 1
    }
)

