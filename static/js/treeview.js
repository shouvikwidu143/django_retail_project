function isArray(obj) {
    return Object.prototype.toString.call(obj) === "[object Array]";
}

function isJson(obj) {
    return Object.prototype.toString.call(obj) === "[object Object]";
}

function isString(obj) {
    return Object.prototype.toString.call(obj) === "[object String]";
}

function makeNonEditable(event) {
    if (event.target.getAttribute("class") != "node-value") {
        editableProperty = document.getElementsByClassName("node-value");
        for (var i = 0; i < editableProperty.length; i++) {
            editableProperty[i].setAttribute("contenteditable", false);
        }
    }
}
function putTableData(data) {
    console.log("In table");
    let tableDiv = document.querySelector(".table-content");
    var rawData = "<table><thead><tr><th>Property</th><th>Value</th></tr></thead><tbody>"; //</tbody>
    for (var key in data) {
        console.log("In data");
        valueOfKey = "";
        if (!isString(data[key])) {
            valueOfKey = JSON.stringify(data[key]);
        } else {
            valueOfKey = data[key];
        }
        rawData += "<tr><td>" + key + "</td><td class=\"node-value\" contenteditable=\"false\">" + valueOfKey + "</td></tr>";
    }
    console.log("Out table");
    rawData += "</tbody></table>";
    tableDiv.innerHTML = rawData;
}

console.log("Treeview");
$(".child").click((event) => {
    console.log(event);
    event.stopPropagation();
    parentNode = event.target.parentNode;
    path = $(parentNode).attr("id");
    checkChild =
        $(parentNode).children("ul.parent").length > 0 ? true : false;
    if (!checkChild && path != undefined) {
        url = `https://jsonplaceholder.typicode.com${path}`;
        fetch(url)
            .then((response) => response.json())
            .then((results) => {
                console.log(Object.prototype.toString.call(results));
                if (isArray(results)) {
                    $(parentNode).append('<ul class="parent">');
                    imChild = $(parentNode).children("ul.parent");
                    results.map((result) => {
                        let contentName = result.name === undefined ? result.title : result.name
                        imChild.append(`<li class="child" id="${path}/${result.id}">
                                    <span class="tree-icon"></span>
                                    <span class="tree-content">${contentName}</span>
                                </li>`);
                    });
                    $(parentNode).append("</ul>");
                    $(parentNode).children("span.tree-icon").toggleClass("tree-icon-down");
                } else if (isJson(results)) {
                    console.log("Json Response received.");
                    putTableData(results);
                }
            });

    } else {
        $(parentNode).children("ul.parent").toggleClass("hide");
        $(parentNode).children("span.tree-icon").toggleClass("tree-icon-down");
    }
});

contentEditable = false;
$(document).on('dblclick', '.node-value', function (event) {
    console.log("Here");
    makeNonEditable(event);
    event.stopPropagation();
    $(this).attr("contenteditable", !contentEditable)

})

$(document).on('click', event=> makeNonEditable(event));