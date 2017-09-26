---
author:
- Đorđe Obradović
subtitle: Univerzitet Singidunum
title: Uvodno predavanje
titlepage-note: |
  This is a the note that goes on the title page. This talk is to be
  given at Doing DH.
institute: George Mason University
fontsize: 17pt
...

# Uvod


\note{}

---

## Sintaksa

Regular text size

\tiny Jonathan Sarna, *American Judaism* (New Haven: Yale University
Press, 2014)

\note{
NOTES: This is a note page and you ought to be able to tell.
}

## Slide with text and footnote

Surely this is true.^[Jane Doe, *Says It Here* (New York: Oxford
University Press, 2050).]

\note{I am sure about this point.}

## This is a heading

Regular text on a slide:

-   One
-   Two
-   Three

\note{
More notes:

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At
vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren,
no sea takimata sanctus est Lorem ipsum dolor sit amet.
}

## Code example

``` {.ruby}
puts "Hello world."
def my_awesome_variable
  puts "My awesome variable"
end
```

\note{
This might be easier in R or Ruby.
}

# Primer sortiranja

- asd ad ada
\note{}
---

## Python

## Code example

``` {.python}
def my_awesome_variable:
  a = "My awesome variable"

```



# Zaključak

\note{}

---

## Python

## Code example

``` {.python}
def get_tasks_excell(idFarms):
    tasks = Tasks().find_by_idFarm(idFarms)
    boxes = {}
    for task in tasks:
        boxId = task['boxId']
        task['status'] = ''
        if boxId in boxes:
            if task['operation'] == 'Berba':
                if task['state'] == '0':
                    task['status'] = '-'
```

## Code example2
``` {.cpp}
int main(string args[]){
  int i=0;
  i++;
}

```
