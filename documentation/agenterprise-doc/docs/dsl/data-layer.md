---
hide:
  - toc
---
# Data Layer

## Entities 
Example:
```dsl
data{
    entity "Restaurant Answer" {
        uid = aiurn:entity:id:restaurantanswer 
        element = aiurn:entity:var:answer -> TEXT # "The answer of the metre"
        element = aiurn:entity:var:restaurant -> aiurn:entity:id:restaurant  # "The restaurant of the metre"
        element = aiurn:entity:var:rating -> NUMBER # "The rating of the restaurant"

    }
```
### Specs
Give the Entity a name by assign a name to entity %MY_NAME% { ... }

| Attribute | Assignment | Rule  | Cardinality  | Examples |
| --------  | --------   | -------- | -------- | -------- |
| uid       | aiurn:entity:id:%Entity_ID% | append %Entity_ID%  to _aiurn:entity:id:_ the identifier of your entity | 1..1 | uid = aiurn:entity:id:restaurantanswer 
| element | aiurn:entity:var:%Variable_Name% | Specify ```TEXT```, ```NUMBER```, ```BOOL```, ```LIST```, ```DICT```, ```ANY``` or ID of different Entity as variable type <br/> Append ```# My Comment```to describe this field to AI processes | 1:N | * ```aiurn:entity:var:answer -> TEXT # "The answer of the metre"```<br/> ```aiurn:entity:var:restaurant -> aiurn:entity:id:restaurant  # "The restaurant of the metre"```
