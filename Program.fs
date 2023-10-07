open System



let rec input msg func = 
    printfn msg
    let inp = Console.ReadLine()
    try func inp with ex -> input "Неверный ввод" func



let splitter (str: string) (x: string) = 
    x.Split([|str|], StringSplitOptions.None)

    

let wspaceSplitter = splitter " "


let factorial (x: int) = 
    match x with
    | 0 -> 1
    | _ -> [1..x] |> List.reduce (fun x y -> x * y)




let intToBool x = 
    match x with
    | 1 -> true
    | _ -> false



let rec series (x: float) (n: int) =
    match n with
    | 1 -> x
    | i when i < 0 -> failwith "n меньше 1"
    | _ -> 
        let mult =  if n / 2 % 2 |> intToBool then -1. else 1.
        mult * x**float(n) / float(factorial n) + series x (n-2)



let task1 () =
    let x = input "Введите вещественное число x" float
    printfn "Вычисленное число: %f" (series x 13)



let NonNeg x = 
    if x >= 0 then x
    else failwith "отрицательное число"



let rec intToDigits (x: int) = 
    let digit = x % 10
    let div = x / 10
    match div with
    | 0 -> [digit]
    | _ -> 
    digit :: intToDigits div



let Translate (x: int) =
    match x with 
    | 0 -> "Нуль"
    | 1 -> "Один"
    | 2 -> "Два"
    | 3 -> "Три"
    | 4 -> "Четыре"
    | 5 -> "Пять"
    | 6 -> "Шесть"
    | 7 -> "Семь"
    | 8 -> "Восемь"
    | 9 -> "Девять"
    | _ -> failwith "ошибка"



let applyAndJoin f str x =
    List.map f x |> String.concat str



let dict = applyAndJoin Translate " "



let task2 () =
    let n = input "Введите натуральное число N" (int >> NonNeg)
    let digits = intToDigits n |> List.rev
    let out = dict digits
    printfn $"{n} -> {out}" 

//task2()



let percent x =
    x / 100.



let floatToN f (x: float) = 
    if x>=0 then
        match x % 1. with
        | 0. -> f x
        | _ -> failwith "ошибка"
    else failwith "ошибка"

let floatToNFloat = floatToN float


let rec growth (x: float) y z= 
    match z with
    | 0. -> x
    | _ -> x + growth (x*y) y (z-1.)



let task3() = 
    let ns = input "Введите начальную популяцию, прирост в процентах и кол-во дней" (wspaceSplitter >> Array.map (float >> floatToNFloat))
    let n = ns.[0]
    let g = ns.[1] / 100.
    let d = ns.[2]
    let newn = growth n g d
    printfn $"Начальная популяция: {n}\n\
    прирост в процентах: {g}\n\
    кол-во дней: {d}\n\n\
    Новая популяция: {newn}"


//task3()


let rec choose n k =
    match k with
    | 0. -> 1.
    | ki when ki > n/2. -> choose n (n-k)
    | _ -> n * choose (n-1.) (k-1.) / k



let binom n =
    let k = [0..n]
    [for i in k do choose (float n) (float i)]



let floatToNInt = floatToN int



let rec triang (n: int) =
    match n with
    | 0 -> ["1"]
    | _ ->  
    let coefs = binom n |> List.map string |> String.concat " "
    coefs :: triang (n-1)



let rec IOtriang l max = 
    match l with 
    | [] -> ()
    | _ -> 
    let head = l.Head
    let dif = (max - String.length head) / 2
    let pad = String.replicate dif " "
    printfn "%s" (pad + head + pad)
    IOtriang l.Tail max



let task4 () =
    let ns = input "Введите число строк треугольника" (float >> floatToNInt)
    let rows = triang ns 
    let rowsRev = List.rev rows
    let max = rows.Head |> String.length
    IOtriang rowsRev max


//task4 ()