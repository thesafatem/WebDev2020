function newElement() {

  var li = document.createElement("li");

  // task name
  var inputText = document.getElementById("input").value;
  if (inputText == "") {
    alert("Task can not be empty!");
    return;
  }
  var t = document.createTextNode(inputText);

  // task icon
  var img = document.createElement("img");
  img.src = "./images/trash.png";
  img.className = "trash-icon";

  // build task
  li.appendChild(t);
  li.appendChild(img);

  // done task
  li.className = "undone li";
  li.onclick = function isDone() {
    if (li.className == "undone li") {
      li.className = "done li";
    } else {
      li.className = "undone li";
    }
  }

  // delete task
  img.onclick = function deleteTask() {
    var liParent = this.parentElement;
    liParent.remove();
  }

  document.getElementById("ulist").appendChild(li);
  document.getElementById("input").value = "";
}



