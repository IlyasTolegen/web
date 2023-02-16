const todoList = document.getElementById("todo-list");
const todoInput = document.getElementById("todo-input");

let items = [];

function addItem() {
  const newItem = todoInput.value.trim();
  if (newItem !== "") {
    items.push({ text: newItem, done: false });
    renderItems();
    todoInput.value = "";
  }
}

function markAsDone(index) {
  items[index].done = !items[index].done;
  renderItems();
}

function deleteItem(index) {
  items.splice(index, 1);
  renderItems();
}

function renderItems() {
  todoList.innerHTML = "";
  for (let i = 0; i < items.length; i++) {
    const item = items[i];
    const listItem = document.createElement("li");
    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.checked = item.done;
    checkbox.addEventListener("change", () => markAsDone(i));
    const text = document.createElement("span");
    text.textContent = item.text;
    if (item.done) {
      listItem.classList.add("done");
    }
    const deleteButton = document.createElement("button");
    deleteButton.textContent = "Delete";
    deleteButton.addEventListener("click", () => deleteItem(i));
    listItem.appendChild(checkbox);
    listItem.appendChild(text);
    listItem.appendChild(deleteButton);
    todoList.appendChild(listItem);
  }
}