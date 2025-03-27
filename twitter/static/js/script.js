let loadUserData = () => {
	return (
		JSON.parse(localStorage.getItem("data")) || {
			loggedInUser: "null",
			loggedInName: "null"
		}
	);
};

let appState = loadUserData();

const getData = async () => {

	document.getElementById("displayHandle").innerText =
		`@${appState.loggedInUser}`;
	document.getElementById("displayName").innerText =
		`${appState.loggedInName}`;
}

getData();

let textArea = document.querySelector('#contentsBox');
let tweetList = []
let id = 0;

let charCountArea = document.getElementById('charCountArea');
    
    // Función para contar caracteres y mostrar los errores de longitud
    let countChar = () => {
        let remainingChar = 280 - textArea.value.length; // Calcula los caracteres restantes
        if (remainingChar < 0) {
            // Si se exceden los caracteres, mostramos el contador en rojo
            charCountArea.innerHTML = `${remainingChar}`.fontcolor('red');
        } else {
            // Si está dentro del límite, mostramos en blanco
            charCountArea.innerHTML = `${remainingChar}`.fontcolor('white');
        }
    }

    // Configura el evento de 'input' para actualizar el contador cada vez que el usuario escribe
    textArea.addEventListener('input', countChar);
    
    // Llama la función de contar caracteres al cargar la página
    countChar();


//Para busqueda
$(document).ready(function() {
    $('#searchInput').on('input', function() {
        let query = $(this).val();
        
        $.ajax({
            url: '/search/',
            data: { query: query },
            success: function(data) {
                $('#searchResults').html(data);  // Mostrar los resultados sin recargar la página
            }
        });
    });
});