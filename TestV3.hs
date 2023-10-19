import Test.HUnit
import V3

-- Definimos algunos vectores para usar en las pruebas
v1 :: Vector3Di Int
v1 = Vector3Di (1, 2, 3)

v2 :: Vector3Di Int
v2 = Vector3Di (4, 5, 6)

-- Definimos algunas pruebas unitarias para cada operación
testSuma :: Test
testSuma = TestCase (assertEqual "Suma de vectores" (Vector3Di (5, 7, 9)) (v1 + v2))

testResta :: Test
testResta = TestCase (assertEqual "Resta de vectores" (Vector3Di (-3, -3, -3)) (v1 - v2))

testProducto :: Test
testProducto = TestCase (assertEqual "Producto vectorial" (Vector3Di (-3, 6, -3)) (v1 * v2))

testModulo :: Test
testModulo = TestCase (assertEqual "Módulo de un vector" (sqrt 14) ((&) v1))

testProductoEscalar :: Test
testProductoEscalar = TestCase (assertEqual "Producto escalar" 32 (v1 % v2))

-- Agrupamos todas las pruebas en una lista
tests :: [Test]
tests = [testSuma, testResta, testProducto, testModulo, testProductoEscalar]

-- Ejecutamos las pruebas y mostramos los resultados
main :: IO ()
main = do
  counts <- runTestTT (TestList tests)
  print counts
