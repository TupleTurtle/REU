open System


let rec input msg tp =
    printfn msg
    let x = Console.ReadLine ()
    try tp x
    with ex -> input "Была допущена ошибка, повторите попытку" tp


let strToArr (x:string) (str:string) = 
    x.Split([|str|], StringSplitOptions.None)


let strToPoint (str:string) =
    str.Split([|','|]) |> Array.map float 


let splitter (x : string) = 
    strToArr x " " |> Array.map strToPoint 


let pow2 x = 
    x**2.


let dist (x: float[]) y = 
    Array.map2 (fun x y -> x - y) x y 
    |> Array.map pow2
    |> Array.sum
    |> sqrt


let task1 () = 
    printfn "Задача 1"
    let coords = input "Введите координаты в формате x1,y1 x2,y2" splitter
    let d = dist coords[0] coords[1]
    printfn $"Расстояние между точками с координатами ({coords[0][0]}, {coords[0][1]}) \
    и ({coords[1][0]}, {coords[1][1]}) = {d}" 


//task1()


let rec allDists (x: float[][]) dists = 
    let el = x[0]
    let x = x[1..]
    let dists = dists @ [for point in x do dist el point]
    match x with
    | [| a |] -> dists
    | _ -> allDists x dists


let pyth x y sgn= 
    x**2. + sgn * y**2. |> sqrt


let norm x =
    Array.map pow2 x |> Array.sum |> sqrt


let arr_mult x y = 
    Array.map2 (fun x y -> x * y) x y |> Array.sum


let cos (x: float[]) y = 
    let xy= arr_mult x y
    let n = norm x * norm y
    printfn $"{xy},{n}, {norm x}, {norm y}" 
    xy / n


let task2 () = 
    printfn "Задача 2"
    let coords = input "Введите координаты в формате x1,y1 x2,y2 x3,y3" splitter
    let lengths = allDists coords List.Empty
    let p = List.sum lengths
    let c = cos coords[1] coords[2]
    let h = c * lengths[0]
    let s = h * lengths[1] / 2.
    printfn $"У треугольника с координатами вершин:\
    ({coords[0][0]}, {coords[0][1]}), \
    ({coords[1][0]}, {coords[1][1]}), \
    ({coords[2][0]}, {coords[2][1]}) \
    периметр = {p}  и площадь = {s}, высота {h}"


//task2()


let namedNum (x: string[]) = 
    (string x[0], float x[1])


let auto x = 
    strToArr x " " |> namedNum


let task3 () = 
    printfn "Задача 3"
    let (n1, v1) = input "Введите имя 1-ого авто и его скорость через пробел" auto
    let (n2, v2) = input "Введите имя 2-ого авто и его скорость через пробел" auto
    let data = input "Введите начальное расстояние и время в формате: S,T" strToPoint
    let d = data[0] - data[1] * (v1 + v2) |> abs
    printfn $"Автомобили с характеристиками:\n\
    1 - {n1}, {v1}\n\
    2 - {n2}, {v2}\n\
    при начальном удалении друг от друга на расстоянии = {data[0]}\n\
    будут на расстоянии {d} через {data[1]} час/часов"


//task3()


let midpoint (x: float[]) y = 
    Array.map2 (fun x y -> (x + y)/2.) x y

let task4 () =
    printfn "Задача 4"
    let coords = input "Введите координаты концов отрезка в формате: x1,y1 x2,y2" splitter
    let mid = midpoint coords[0] coords[1]
    printfn $"Середина отрезка с координатами концов: ({coords[0][0]}, {coords[0][1]})\
    и ({coords[1][0]}, {coords[1][1]})\n\
    имеет координаты: ({mid[0]}, {mid[1]})"


//task4()


let task5 () = 
    printfn "Тема3, Задача 1"
    let nums = input "Введите x и y в формате: x,y" strToPoint
    let x = nums[0]
    let y = nums[1]
    let body x y = 
        if x > y then x - y
        else y - x + 1.
    printfn "%f" (body x y)



//task5()
let kind (sides: List<float>) =
    let arr = [|sides[0] = sides[1]; sides[0]=sides[2]; sides[1]=sides[2]|]
    if List.contains 0. sides then "Не треугольник" else
    let count = Array.filter (fun x -> x=true) arr
    match Array.length count with
    | 3 -> "Равносторонний"
    | 1 -> "Равнобедренный"
    | _ -> if sides[0]+sides[1]>sides[2] then "Разносторонний" else "Не треугольник"


let task6 () = 
    printfn "Тема3, Задача 2"
    let coords = input "Введите координаты в формате: x1,y1 x2,y2 x3,y3" splitter
    let sides = allDists coords [] |> List.map (fun x -> float(int (x * 10.)) / 10.)
    let cls = kind sides
    printfn $"Треугольник с координатами вершин:\
    ({coords[0][0]}, {coords[0][1]}), \
    ({coords[1][0]}, {coords[1][1]}), \
    ({coords[2][0]}, {coords[2][1]})\n\
    имеет длины сторон: {sides[0]}, {sides[1]}, {sides[2]}\n\
    вид треугольника: {cls} "
    //ratio x/y = 0.25605276998


//task6()

let in_inter x start finish =
    if x>=start && x<= finish then true
    else false


let check_len (x:float) l =
    let modulo = x / 10.**(l-1.)
    in_inter modulo 1. 9.999999999999


let task7 () = 
    printfn "Тема3, Задача 3"
    let num = input "Введите число" float
    let body x = 
        if check_len x 4. && (x % 77. = 0. || x % 1717. = 0.) then true else false
    let res = body num
    printf (if res then "Красивое число" else "Некрасивое число")


//task7()


let even (x: float[]) y = 
    let diff = Array.map2 (fun x y -> x-y |> abs) x y |> Array.sum 
    match diff % 2. with
    | 1. -> false
    | _ -> true
    


let task8 () =
    let coords = input "Введите координаты клетки в формате x1,y1 x2,y2" splitter
    printfn (
    if even coords[0] coords[1] then "Клетки одного цвета" 
    else "Клетки разного цвета")


//task8()