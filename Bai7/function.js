function changeColor()
{
    document.getElementById("text1").style.color='blue'
    document.getElementById("text2").style.color='yellow'
    document.getElementById("text3").style.color='red'
}
function changeBGColor(color)
{
    return document.body.style.background = color
}
function copyContent(paragraph1, paragraph2)
{
   let h1 = document.getElementById(paragraph1)
   let h2 = document.getElementById(paragraph2)
   let h3 = h1.innerText
   h1.innerText = h2.innerText
   h2.innerText = h3
}
function changeFontSize(x)
{
    document.querySelectorAll('p')[0].style.fontSize = x
    document.querySelectorAll('p')[1].style.fontSize = x
    document.querySelectorAll('p')[2].style.fontSize = x
}
function increaseFontSize(paragraph)
{
    let f1 = document.getElementById(paragraph).style.fontSize
    f1 = parseFloat(f1)
    f2 = f1+10
    if (f2 > 30)
    {
        return "Không tăng"
    }
        
    else{
        document.getElementById(paragraph).style.fontSize = f2+'px'
    }
   
}
function decreaseFontSize(paragraph)
{
    let f1 = document.getElementById(paragraph).style.fontSize
    f1 = parseFloat(f1)
    f2 = f1-1
    if (f1 < 10)
    {
        return ("Không giảm")
    }
        
    else{
    document.getElementById(paragraph).style.fontSize = f2+'px'
    }
}