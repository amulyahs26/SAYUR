document.addEventListener("DOMContentLoaded", function() {
    fetchTasks();
});

function fetchTasks() {
    fetch('/tasks')
        .then(response => response.json())
        .then(data => {
            const taskList = document.getElementById('task-list');
            taskList.innerHTML = '';
            data.forEach(task => {
                const li = document.createElement('li');
                li.textContent = task.text;
                if (task.done) {
                    li.classList.add('done');
                }
                li.addEventListener('click', () => toggleTask(task._id));
                taskList.appendChild(li);
            });
        });
}

function addTask() {
    const newTaskInput = document.getElementById('new-task');
    const taskText = newTaskInput.value.trim();

    if (taskText) {
        fetch('/tasks', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ text: taskText })
        }).then(() => {
            newTaskInput.value = '';
            fetchTasks();
        });
    }
}

function toggleTask(id) {
    fetch(`/tasks/${id}/toggle`, {
        method: 'PATCH'
    }).then(() => {
        fetchTasks();
    });
}
