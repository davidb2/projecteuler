import std/algorithm
import std/sugar
import std/sequtils
import std/sets
import std/setutils

type Info = object
  filled: bool
  componentId: int

type Result = object
  cells: seq[Info]
  maxConnected: int

iterator fillingsRec(width: int, acc: var seq[bool]): seq[bool] {.closure.} =
  if width <= 0:
    yield acc
    return

  for val in false..true:
    acc.add(val)
    defer: discard acc.pop()
    let rec = fillingsRec
    for xs in rec(width-1, acc):
      yield xs

iterator fillings(width: int): seq[bool] =
  var acc: seq[bool] = @[]
  for filling in fillingsRec(width, acc):
    yield filling

iterator newResults(row: Result): Result =
  let usedComponentIds = block:
    row
      .cells
      .filter(info => info.filled)
      .map(info => info.componentId)
      .deduplicate
      .sorted
      .toHashSet

  var unusedComponentIds = block:
    (0..<row.cells.len)
      .toSeq
      .filter(id => id notin usedComponentIds)
      .toHashSet

  for filling in fillings(width=row.cells.len):
    var newRow = Result(cells: @[], maxConnected: 0)
    for (filled, info) in zip(filling, row.cells):
      newRow.cells.add(Info(
        filled: filled,
        componentId: block:
          if not filled: -1
          elif info.filled: info.componentId
          elif newRow.cells.len > 0 and newRow.cells[^1].filled: newRow.cells[^1].componentId
          else: unusedComponentIds.pop()
      ))
    yield newRow

# proc _expectedMax(height, width: int, prevRow: Result): Result =
#   discard
# 
# proc expectedMax(width, height: int): Result =
#   discard


when isMainModule:
  echo "hi"
  for xs in fillings(3):
    echo xs

  let row = Result(cells: @[Info(filled: true, componentId: 0)], maxConnected: 0)
  for res in newResults(row):
    echo res
  # echo pow(@[false, true], 3)
