open System


let split (sym: string) (s: string) = 
    s.Split([|sym|], StringSplitOptions.None)

let wsSplit = split " "
let cSplit = split ","


let two (x: float[]) =
    let l = x.[1..]
    if x.[0] = float l.Length then l else failwith "Длина не соответствует указанной"

let twoI (x: int[]) =
    let l = x.[1..]
    if x.[0] = l.Length then l else failwith "Длина не соответствует указанной"

let rec inp msg f = 
    printfn "%s" msg
    let i = Console.ReadLine()
    try f i with ex -> inp "Неправильный ввод" f



let suffice (x:float) = x % 3. = 0. && x % 5. <> 0.


let task1 () = 
    let l = inp "Введите кол-во элементов и список вещественных чисел" (wsSplit >> Array.map float >> two)
    let nl = Array.filter suffice l
    printfn $"Исходный список: %A{l}\n Кол-во удовл. элементов: {nl.Length}\n\
              Сумма удовл. элементов: {Array.sum nl}"


let check (x: float[]) = 
    x.Length = 2 



let apply (l: float[][]) = 
    let rec loop acc (l: float[][]) =
        if l = [||] then List.rev acc 
        else
            match l.[0] with
            | [|a; b|] -> loop ((a, b)::acc) l.[1..]
            | _ -> loop acc l.[1..]
    loop [] l



let task2 () = 
    let l = inp "Введите список вещественных чисел" (wsSplit >> Array.map float)
    let nl = Array.chunkBySize 2 l |> apply 
    printfn $"Исходный список: %A{l}\n\
              Новый список: %A{nl}"




let task3 () = 
    let l = inp "Введите число значений и список для главного и доп списка в формате X x1 x2 x3,\
                 Y y1 y2 y3" (cSplit >> Array.map (wsSplit >> Array.map int >> twoI))

    let l1 = l.[0]
    let l2 = l.[1]


    let nl = Array.filter (fun x -> not (Array.contains x l2)) l1
    printfn $"Исходный список: %A{l1}\n\
              Список разрешенных значений: %A{l2}\n\
              Новый список: %A{nl}\n\
              Число элементов нового списка: {nl.Length}"


let generate l =
    let rec loop acc = function
    | [a] -> List.rev acc
    | [] -> List.rev acc
    | x::xs -> loop (acc.Head+x::acc) xs
    loop [0] l




let task4 () = 
    let l = inp "Введите кол-во элементов и список вещественных чисел" (wsSplit >> Array.map int >> twoI >> Array.toList)
    let t = generate l
    let maxi = List.max l
    let mini = List.min l
    let isMaxMin = List.map (fun x -> (x = maxi, x = mini)) l
    let customers = List.zip3 l t isMaxMin
    for c in List.zip [1..l.Length] customers do
        let serv, wait, mm = snd c
        printfn $"Номер: {fst c} | Время обслуживания: {serv} |\
                  Время ожидания: {wait} | Макс или мин: {mm}"





let rec merge (l1: list<float>) (l2: list<float>) acc =
    if l1 = [] then 
        if l2 = [] then acc 
        else merge l1 l2.Tail (l2.Head::acc) 
    elif l2 = [] then merge l1.Tail l2 (l1.Head::acc) 
    else
        let h1 = l1.Head
        let h2 = l2.Head
        if h1 <= h2 then merge l1.Tail l2 (h1::acc)
        else merge l1 l2.Tail (h2::acc)


printfn $"%A{merge [1.; 2.; 3.] [3.; 4.; 5.; 6.; 7.] []}"    

        



let rec mergeSort l = 
    match l with
    | [a] -> l
    | _ -> 
        let half = l.Length/2 
        merge l.[..half] l.[half+1..] []


printfn $"%A{mergeSort [7.; 2.; 3.; 5.; 1.]}"    


