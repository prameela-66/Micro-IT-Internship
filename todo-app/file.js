function addTask() {
    let taskInput = document.getElementById("taskInput");
    let taskText = taskInput.value.trim();
    if (taskText === "") return;

    let taskList = document.getElementById("taskList");
    let li = document.createElement("li");
    li.innerHTML = `<span>${taskText}</span>
                    
                    <button onclick="removeTask(this)" style="background:none; color: grey;">✖</button>`;
    taskList.appendChild(li);
    taskInput.value = "";
}

function completeTask(button) {
    let taskItem = button.parentElement;
    taskItem.firstChild.classList.toggle("completed");
}

function removeTask(button) {
    let taskItem = button.parentElement;
    taskItem.remove();
}
