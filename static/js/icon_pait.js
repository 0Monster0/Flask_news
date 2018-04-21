window.onload = function () {  
    function icon_pait() {  
        var pDowns = document.querySelectorAll(".icon_down");  
        for(var i in pDowns){  
            var pDowni = pDowns.item(i);  
            var pDown = pDowni.getContext("2d");  
            pDown.lineWidth = 2;  
            pDown.moveTo(17,6);  
            pDown.lineTo(17,18);  
            pDown.moveTo(11,13);  
            pDown.lineTo(17,18);  
            pDown.lineTo(23,13);  
            pDown.moveTo(9,17);  
            pDown.lineTo(9,22);  
            pDown.lineTo(25,22);  
            pDown.lineTo(25,17);  
            pDown.stroke();  
        }  
        var pSearch = document.getElementById("icon_search").getContext("2d");  
        pSearch.strokeStyle = "#999";  
        pSearch.arc(10,10,4,0,7);  
        pSearch.moveTo(13,13);  
        pSearch.lineTo(17,17);  
        pSearch.stroke();  
    }  
    icon_pait();  
    var bool = true;  
    window.onscroll = function () {  
        var scrollTop = document.documentElement.scrollTop || document.body.scrollTop;  
        if(bool && scrollTop>1248){  
            bool = false;  
            var sideBox = document.getElementById("sideBox");  
            sideBox.innerHTML = "";  
            sideBox.style.display = "block";  
            sideBox.appendChild(document.getElementById("searchBox").cloneNode(true));  
            sideBox.appendChild(document.getElementById("erweima").cloneNode(true));  
            icon_pait();  
        }else if(!bool && scrollTop<1000){  
            var sideBox0 = document.getElementById("sideBox");  
            sideBox0.style.display = "none";  
            sideBox0.innerHTML = "";  
            bool = true;  
        }  
    };  
    var timeOut = 0;  
    document.getElementById("menuMore").addEventListener("mouseover",function () {  
        clearTimeout(timeOut);  
        document.getElementById("menuMorePanel").style.display = "block";  
    });  
    document.getElementById("menuMore").addEventListener("mouseout",function () {  
        timeOut = setTimeout(function () {  
            document.getElementById("menuMorePanel").style.display = "none";  
        },150);  
    });  
}; 