var
    a, b, c, i, ans: integer;
begin
    read(a, b, c);

    b := b mod 4;

    if b = 2 then 
        if c = 1 then b := 2
        else b := 0
    else if c mod 2 = 1 then b := b mod 4
    else b := b * b mod 4;

    if b = 0 then b := 4;

    a := a mod 10;
    ans := 1;
    for i := 1 to b do ans := ans * a mod 10;
    
    write(ans)
end.