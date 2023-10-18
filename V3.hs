-- Implementa un modulo de vectores de 3 dimensiones con las siguientes características:
module V3 where

-- Define un nuevo tipo de datos para representar vectores de 3 dimensiones
newtype Vector3Di a = Vector3Di (a, a, a)

-- Implementa las operaciones de suma, resta, producto vectorial, módulo y producto escalar.
instance (Eq a) => Eq (Vector3Di a) where
  (==) :: Vector3Di a -> Vector3Di a -> Bool
  (Vector3Di (i, j, k)) == (Vector3Di (x, y, z)) = i == x && j == y && k == z

instance (Num a) => Num (Vector3Di a) where
  (+) :: Vector3Di a -> Vector3Di a -> Vector3Di a
  (Vector3Di (i, j, k)) + (Vector3Di (x, y, z)) = Vector3Di (i + x, j + y, k + z)

  (-) :: Vector3Di a -> Vector3Di a -> Vector3Di a
  (Vector3Di (i, j, k)) - (Vector3Di (x, y, z)) = Vector3Di (i - x, j - y, k - z)

  (*) :: Vector3Di a -> Vector3Di a -> Vector3Di a
  (Vector3Di (i, j, k)) * (Vector3Di (x, y, z)) = Vector3Di (j * z - k * y, k * x - i * z, i * y - j * x)

  -- Funciones necesarias para el tipo Num
  abs :: Vector3Di a -> Vector3Di a
  abs (Vector3Di (i, j, k)) = Vector3Di (abs i, abs j, abs k)

  signum :: Vector3Di a -> Vector3Di a
  signum (Vector3Di (i, j, k)) = Vector3Di (signum i, signum j, signum k)

  fromInteger :: Integer -> Vector3Di a
  fromInteger n = Vector3Di (fromInteger n, fromInteger n, fromInteger n)

-- implementa el Producto escalar
infixl 7 %

(%) :: (Num a) => Vector3Di a -> Vector3Di a -> a
(Vector3Di (i, j, k)) % (Vector3Di (x, y, z)) = i * x + j * y + k * z

-- Implementa el Módulo
infixl 9 &

(&) :: (Floating a) => Vector3Di a -> a
(&) (Vector3Di (i, j, k)) = sqrt (i ^ 2 + j ^ 2 + k ^ 2)

-- Implementa la instancia de Show para que se muestren los vectores de la forma (i, j, k)
instance (Show a) => Show (Vector3Di a) where
  show :: Vector3Di a -> String
  show (Vector3Di (i, j, k)) = "(" ++ show i ++ ", " ++ show j ++ ", " ++ show k ++ ")"
