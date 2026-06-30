from typing import optional1

name:str = "fiza"
age:int = 21
price:float = 49.94
is_member:bool = True
tag:list[str]= ["ai","python"]
scores:dict[str,int] = {"math":87,"science":89}
nickname:optional1[str]=None

def total_price(price:float,qty:int) -> float:
    return price * qty
