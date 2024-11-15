const starterTodos = [
    { userId: 1, id: 1, title: "Learn how to use localStorage", completed: false },
    { userId: 1, id: 2, title: "Understand sessionStorage and its limitations", completed: false },
    { userId: 1, id: 3, title: "Set and retrieve data using cookies", completed: false },
    { userId: 1, id: 4, title: "Practice CRUD operations with localStorage", completed: false },
    { userId: 1, id: 5, title: "Explore security considerations for cookies", completed: false }
];

let todos = JSON.parse(localStorage.getItem('todos')) || starterTodos;
let filter = 'all';

function saveTodos() {
    localStorage.setItem('todos', JSON.stringify(todos));
}

function renderTodos() {
    const list = document.getElementById('todo-list');
    list.innerHTML = '';

    const filteredTodos = todos.filter(todo =>
        filter === 'all' ||
        (filter === 'active' && !todo.completed) ||
        (filter === 'completed' && todo.completed)
    );

    filteredTodos.forEach(todo => {
        const li = document.createElement('li');
        li.className = todo.completed ? 'completed' : '';
        li.innerHTML = `
      <input type="checkbox" ${todo.completed ? 'checked' : ''} onclick="toggleComplete(${todo.id})">
      <span contenteditable="true" onblur="editTask(${todo.id}, this)">${todo.title}</span>
      <button onclick="deleteTask(${todo.id})">Delete</button>
    `;
        list.appendChild(li);
    });
}

function addTask() {
    const input = document.getElementById('new-todo');
    const title = input.value.trim();
    if (title) {
        todos.push({ userId: 1, id: Date.now(), title, completed: false });
        input.value = '';
        saveTodos();
        renderTodos();
    }
}

function deleteTask(id) {
    todos = todos.filter(todo => todo.id !== id);
    saveTodos();
    renderTodos();
}

function toggleComplete(id) {
    const todo = todos.find(todo => todo.id === id);
    if (todo) {
        todo.completed = !todo.completed;
        saveTodos();
        renderTodos();
    }
}

function editTask(id, element) {
    const todo = todos.find(todo => todo.id === id);
    if (todo) {
        todo.title = element.innerText;
        saveTodos();
        renderTodos();
    }
}

function setFilter(newFilter) {
    filter = newFilter;
    renderTodos();
}

// Initial render
saveTodos();
renderTodos();

