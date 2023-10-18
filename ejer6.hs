import System.Environment

choose n k = product [n - k + 1 .. n] `div` product [1 .. k]

narayana n k = (choose n k * choose n (k - 1)) `div` n

fib 0 = 0
fib 1 = 1
fib n = fib (n - 1) + fib (n - 2)

log2 1 = 0
log2 x = 1 + log2 (x `div` 2)

floor1 x = fromIntegral (truncate x)

wadefoc n = fib (floor1 (log2 (narayana (n + 1) (n - 1))) + 1)

main :: IO ()
main = do
  args <- getArgs -- obtiene la lista de argumentos del programa
  let n = read (head args) :: Int -- convierte el primer argumento a un entero
  print (wadefoc n) --