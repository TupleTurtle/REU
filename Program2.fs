// 12 код
open System



let rec input msg func = 
    printfn msg
    let inp = Console.ReadLine()
    try func inp with ex -> input "Неверный ввод" func


    
let intToBool (x: int): bool = 
    if x = 1 then true
    else false



let boolToMult (x: bool): float = 
    if x then -1.
    else 1.



let rec factorial (x: int) = 
    match x with
    | 1 | 0 -> 1
    | _ -> x * factorial (x-1) 



let rec series (x: float) (n: int) =
    match n with 
    | 1 -> x
    | _ ->
    let mult = n / 2 % 2 |> intToBool |> boolToMult
    let step = mult * x ** float n / (n |> factorial |> float)
    step + series x (n-2)

        

let task1 () =
    let x = input "Введите вещественное число x" float
    printfn "Вычисленное число: %f" (series x 13)

//task1()
    

let numToWord (x: char) = 
    match x with
    | '0' -> "Ноль"
    | '1' -> "Один"
    | '2' -> "Два"
    | '3' -> "Три"
    | '4' -> "Четыре"
    | '5' -> "Пять"
    | '6' -> "Шесть"
    | '7' -> "Семь"
    | '8' -> "Восемь"
    | '9' -> "Девять"
    | _ -> failwith "ошибка"
// Делить     


let strToArr (x: string) =
    //x.Split([|""|], StringSplitOptions.None)
    Seq.toArray x



let translate (x: char[]) = 
    [for i in x -> numToWord i] |> String.concat " "



let task2() = 
    let N = input "Введите натуральное число N" (strToArr >> translate)
    printfn "%s" N

//task2()


let rec population (x: int) (m: int) (n: int) = 
    match n with
    | 0 -> x
    | _ -> population (x * m) m (n-1)


let strToArrByWs (x: string) = 
    x.Split([|" "|], StringSplitOptions.None)


let strArrToIntArr x = 
    Array.map int x



let task3() =
    let N = input "Введите начальное кол-во организмов, процент среднесуточного увеличения \
        и количество дней через пробел (все натуральные числа)" (strToArrByWs >> strArrToIntArr)
    let newN = population N.[0] N.[1] N.[2]
    printfn $"Начальное кол-во организмов: {N.[0]}\n\
              Процент среднесуточного увеличения: {N.[1]}n\
              Количество дней: {N.[2]}\n\n\
              Новое население: {newN}"

//task3()
// брать процент а не натуральное


let C n k =
    factorial n / (factorial k * factorial (n-k))



let binom n = 
    let k = [0..n]
    List.map (fun x -> string (C n x)) k |> String.concat " "



let pascal n = 
    for i in [0..n] do printfn "%s" (binom i)


    
let task4() = 
    let x = input "Введите вещественное число строчек треугольника Паскаля" int
    printfn ""
    pascal (x-1)


task1()
task2()
task3()
task4()

    1
   2 1
  3 2 4