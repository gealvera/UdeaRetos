function formatCurrency(input) {
    // Eliminar caracteres no numéricos
    let value = input.value.replace(/\D/g, "");
    
    // Formatear como moneda
    value = new Intl.NumberFormat("es-CO", {
        style: "currency",
        currency: "COP",
        minimumFractionDigits: 0
    }).format(value);
    
    // Actualizar el valor del campo de entrada
    input.value = value;
}

async function simulatePriorizacion(event) {
    event.preventDefault();

    // Deshabilitar el botón de Simular Priorización
    const btnPriorizacion = document.querySelector("button[type='submit']");
    btnPriorizacion.disabled = true;

    // Obtener y procesar el valor del campo "ingresos"
    const ingresosField = document.getElementById("ingresos");
    const ingresos = ingresosField.value.replace(/\D/g, ""); // Eliminar formato de moneda para obtener solo el número

    const estrato = document.getElementById("estrato").value;

    const costoField = document.getElementById("costo");
    const costo = costoField.value.replace(/\D/g, ""); // Eliminar formato de moneda para obtener solo el número

    // Enviar la solicitud al servidor
    const response = await fetch(`/simulador?Ingresos=${ingresos}&Estrato=${estrato}&Costo=${costo}`);
    const result = await response.json();

    // Actualizar los mensajes y mostrar el segundo formulario si aplica
    const message = document.getElementById("priorizacion-message");
    const resultDiv = document.getElementById("priorizacion-result");
    const energiaForm = document.getElementById("form-energia");

    // Reiniciar estados previos
    resultDiv.style.display = "block";
    message.textContent = result["Predicción de Priorización"];
    message.className = ""; // Limpia clases previas

    // Asignar clases según el resultado
    if (result["Predicción de Priorización"] === "Sí Priorizado") {
        message.classList.add("si");
        energiaForm.style.display = "block"; // Mostrar el segundo formulario
        energiaForm.classList.remove("hidden");
    } else {
        message.classList.add("no");
    }

    // Mostrar el botón "Nueva Simulación"
    document.getElementById("nueva-simulacion").style.display = "inline-block";
}

async function simulateEnergia(event) {
    event.preventDefault();

    // Deshabilitar el botón de Simular Energía Limpia
    const btnEnergia = document.querySelector("#form-energia button[type='submit']");
    btnEnergia.disabled = true;

    // Obtener los valores del formulario
    const radiacion = document.getElementById("radiacion").value;
    const viento = document.getElementById("viento").value;

    // Enviar la solicitud al servidor
    const response = await fetch(`/energia?Radiacion=${radiacion}&Viento=${viento}`);
    const result = await response.json();

    // Mostrar el mensaje de energía recomendada
    const energiaMessage = document.getElementById("energia-message");
    energiaMessage.textContent = `Energía Recomendada: ${result["Energía Recomendada"]}`;
    energiaMessage.className = ""; // Limpia clases previas  

    // Asignar clases según el tipo de energía
    if (result["Energía Recomendada"] === "Solar") {
        energiaMessage.classList.add("solar");
    } else if (result["Energía Recomendada"] === "Eólica") {
        energiaMessage.classList.add("eolica");
    }

    // Mostrar el botón "Nueva Simulación"
    document.getElementById("nueva-simulacion").style.display = "inline-block";
}

async function exportarExcel() {
    window.location.href = "/exportar";
}

function nuevaSimulacion() {

    // Limpiar los campos de los formularios
    document.getElementById("ingresos").value = "";
    document.getElementById("estrato").value = "";
    document.getElementById("costo").value = "";
    document.getElementById("radiacion").value = "";
    document.getElementById("viento").value = "";

    // Limpiar los mensajes y resultados
    const priorizacionResult = document.getElementById("priorizacion-result");
    const priorizacionMessage = document.getElementById("priorizacion-message");
    const energiaMessage = document.getElementById("energia-message");

    priorizacionResult.style.display = "none"; // Ocultar el contenedor de priorización
    if (priorizacionMessage) {
        priorizacionMessage.textContent = ""; // Limpiar texto
        priorizacionMessage.className = "";
    }
    if (energiaMessage) {
        energiaMessage.textContent = ""; // Limpiar texto de energía
        energiaMessage.className = "";
    }

    // Habilitar los botones
    const btnPriorizacion = document.querySelector("#form-priorizacion button[type='submit']");
    if (btnPriorizacion) btnPriorizacion.disabled = false;

    const btnEnergia = document.querySelector("#form-energia button[type='submit']");
    if (btnEnergia) btnEnergia.disabled = false;

    // Ocultar el botón Nueva Simulación
    const nuevaSimulacionButton = document.getElementById("nueva-simulacion");
    if (nuevaSimulacionButton) nuevaSimulacionButton.style.display = "none";

    // Ocultar el formulario de energía
    const energiaForm = document.getElementById("form-energia");
    if (energiaForm) {
        energiaForm.style.display = "none"; // Ocultar con estilo inline
        energiaForm.classList.add("hidden"); // Añadir clase para asegurar ocultamiento
    }
}