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
    let l = inp "Введите кол-во элементов и список вещественных чисел (всё через пробел)" (wsSplit >> Array.map float >> two)
    let nl = Array.filter suffice l
    printfn $"Исходный список: %A{l}\n Кол-во удовл. элементов: {nl.Length}\n\
              Сумма удовл. элементов: {Array.sum nl}"


let check (x: float[]) = 
    x.Length = 2 



let apply (l: float[][]) = 
    let rec loop acc (l: float[][]) i =
        if i = l.Length - 1 then List.rev acc 
        else
            match l.[i] with
            | [|a; b|] -> loop ((a, b)::acc) l (i+1)
            | _ -> List.rev acc 
    loop [] l 0



let task2 () = 
    let l = inp "Введите вещественные числа через пробел" (wsSplit >> Array.map float)
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
    let l = inp "Введите кол-во элементов и целые числа (время обслуживания для каждого покупателя)" (wsSplit >> Array.map int >> twoI >> Array.toList)
    let t = generate l
    let maxi = List.max l
    let mini = List.min l
    let isMaxMin = List.map (fun x -> (x = maxi, x = mini)) l
    let customers = List.zip3 l t isMaxMin
    for c in List.zip [1..l.Length] customers do
        let serv, wait, mm = snd c
        printfn $"Номер: {fst c} | Время обслуживания: {serv} |\
                  Время ожидания: {wait} | Макс или мин: {mm}"




let rec join (x: list<float>) (y: list<float>) = 
    if x.IsEmpty then y
    else join x.Tail (x.Head::y)


let rec merge (x: list<float>) (y: list<float>) (z: list<float>) =
    let xemp = x.IsEmpty
    let yemp = y.IsEmpty
    match (xemp, yemp) with
    | false, false -> 
        let xh = x.Head
        let yh = y.Head
        if xh < yh then merge x.Tail y (xh::z)
        else merge x y.Tail (yh::z)
    | true, false -> join y z |> List.rev
    | false, true -> join x z |> List.rev
    | true, true -> z |> List.rev



let rec mergeSort (x: list<float>) = 
    let len = x.Length
    if len = 0 || len = 1 then x
    else 
        let half = len / 2

        merge (mergeSort x.[..half-1]) (mergeSort x.[half..]) []




let rec heapify (arr: array<float>) i =
    let len = arr.Length
    let ind = i*2+1
    let dif = len - ind
    if dif > 0 then

        heapify arr ind
        let c1 = arr.[ind]
        if c1 > arr.[i] then
            arr.[ind] <- arr.[i]
            arr.[i] <- c1

        if dif - 1 <> 0 then 
            let ind2 = ind+1
            heapify arr ind2
            let c2 = arr.[ind2]
            if c2 > arr.[i] then
                arr.[ind2] <- arr.[i]
                arr.[i] <- c2



let heapSort (x: array<float>) =
    let rec heapSortStep x (acc: array<float>) j= 
        let len = acc.Length
        if j <> len then
            heapify x 0
            acc.[len-j-1] <- x.[0]
            x.[0] <- x.[len-1]
            x.[len-1] <- -infinity
            heapSortStep x acc (j+1)
        else 
            acc
    let xheap = [|for i in x -> i|]
    heapSortStep xheap (Array.zeroCreate x.Length) 0





let randomNumbers n = 
    let rnd = System.Random()
    Array.init n (fun _ -> rnd.Next() |> float)
    //Array.init n (fun _ -> rnd.NextDouble())



let task5() = 
    //let l = inp "Введите список случайных чисел" (wsSplit >> Array.map float)
    let l = randomNumbers 50
    printfn "---------------------\n\n"

    let timeMerge = System.Diagnostics.Stopwatch.StartNew()
    let sortedMerge = l |> Array.toList |> mergeSort
    timeMerge.Stop()
    printfn "---------------------"
    printfn $"Результат сортировки слиянием:\n%A{sortedMerge |> List.toArray}\n\n\
              Время: %A{timeMerge.Elapsed.TotalMilliseconds}\n---------------------\n\n"
    
    let timeHeap = System.Diagnostics.Stopwatch.StartNew()
    let sortedHeap = l |> heapSort
    timeHeap.Stop()
    printfn "---------------------"
    printfn $"Результат пирамидальной сортировки:\n%A{sortedHeap}\n\n\
              Время: %A{timeHeap.Elapsed.TotalMilliseconds}\n---------------------\n\n"

    printfn "---------------------"
    let timeSort = System.Diagnostics.Stopwatch.StartNew()
    let sortedSort = l |> Array.sort 
    timeSort.Stop()
    printfn $"Результат встроенной сортировки:\n%A{sortedSort}\n\n\
              Время: %A{timeSort.Elapsed.TotalMilliseconds}"        
    printfn "---------------------"


task5()
//printfn $"%A{heapSort arr3}"

