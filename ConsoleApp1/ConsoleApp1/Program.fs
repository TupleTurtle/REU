// Learn more about F# at http://docs.microsoft.com/dotnet/fsharp
open System

let num x =
    if (box x :? float || box x :? int) then x 
    else "ввел не число"

let task1 () =
    let inp msg =
        printfn msg
        Console.ReadLine() |> num

    let x1 = inp "первое число" |> int
    let x2 = inp "второе число" |> int

    let z (x: int) y =
        if x > y then x - y
        else y - x + 1

    let zo = z x1 x2

    let out x y z = 
        printfn $"Для x = {x} и y = {y} \n значение z = {zo}"

    out x1 x2 z


let task2 () =

    let inp msg =
        printfn msg
        let txt = Console.ReadLine() |> num |> string
        txt.Split ([|" "|], StringSplitOptions.None)

    let coords = inp "Введите координты в формате x1 x2 y1 y2 z1 z2"

    let t11 = coords.[0] |> float
    let t12 = coords.[1] |> float
    let t21 = coords.[2] |> float
    let t22 = coords.[3] |> float
    let t31 = coords.[4] |> float
    let t32 = coords.[5] |> float
    
    let dist x1 x2 y1 y2 = 
        (x1 - y1) ** 2. + (x2 - y2) ** 2.

    let d1 = dist t11 t12 t21 t22
    let d2 = dist t11 t12 t31 t32
    let d3 = dist t21 t22 t31 t32

    let equilateral d1 d2 d3 = 
        let d1i = d1 |> BitConverter.DoubleToInt64Bits
        let d2i = d2 |> BitConverter.DoubleToInt64Bits
        let d3i = d3 |> BitConverter.DoubleToInt64Bits

        if (d1i = d2i && d1i = d3i) then "Равносторонний"
        elif (d1i = d2i || d2i = d3i || d1i = d3i) then "Равнобедренный"
        elif (d1i+d2i > d3i || d2i+d3i > d1i || d1i+d2i > d2i) then "Обычный треугольник"
        else "Не треугольник"
        
    let kind = equilateral d1 d2 d3
    //let t3 = t2.Split ([","], StringSplitOptions.None)
    printfn $"Треугольник с координатами вершин: ({t11}, {t12}), ({t21}, {t22}), ({t31}, {t32}) \n имеет длины сторон: {d1} {d2} {d3} \n вид треугольника {kind}"


let task3 () =
    

    let inp msg =
        printfn msg
        Console.ReadLine() |> num |> float
      
    
    let fourdigit x = 
        if log10 x >= 3. then true
        else false

    let check x =
        if fourdigit x then
            if (x % 77. = 0. || x % 1717. = 0.) then "Красивое число"
            else "Некрасивое число"
        else "Не четырех значное"

    let x = inp "Введите число"
    let out = check x
    printfn $"{out}"


task3 ()

    

