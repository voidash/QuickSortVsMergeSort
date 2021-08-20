var canvas, width, height, control;

var arr = [], intermediate = [], visited = [];
var qarr = [], qinter = [], qvisited = [];

slider = document.querySelector("#numberOfElements")
var len_of_arr = slider.value;

var widthOfEachBar = 400 / len_of_arr;
var spaceBetweenBars = 100 / len_of_arr;
//get buttons and sliders
runnerButton = document.querySelector(".runner");
numElem = document.querySelector('.numElem');
numElem.innerHTML = slider.value;

slider.addEventListener("change", (event) => {
    numElem.innerHTML = event.target.value;
    len_of_arr = event.target.value;
    spaceBetweenBars = 100 / len_of_arr;
    widthOfEachBar = 400 / len_of_arr;
    for (let i = 0; i < len_of_arr; i++) {
        arr.push(Math.round(Math.random() * 250))
        qarr[i] = arr[i];
        intermediate.push(0);
        qinter.push(0);
        visited.push(0);
        qvisited.push(0);
    }
    drawInitialBars();
});
runnerButton.addEventListener("click", async (event) => {
    MergeSort(0, len_of_arr - 1);
    await QuickSort(0, len_of_arr - 1);
    drawMergeBars(0, len_of_arr);
    drawQuickBars(0, len_of_arr);
});

for (let i = 0; i < len_of_arr; i++) {
    arr.push(Math.round(Math.random() * 250))
    qarr[i] = arr[i];
    intermediate.push(0);
    qinter.push(0);
    visited.push(0);
    qvisited.push(0);
}
function canvasElements() {
    canvas = document.querySelector('#Canvas');
    height = 350;
    width = 1120;
    canvas.width = width;
    canvas.height = height;
    control = canvas.getContext("2d");
}
canvasElements();






function merge(start, end) {

    let partition = parseInt((start + end) / 2);

    let start1 = start, start2 = partition + 1;
    let end1 = partition, end2 = end;
    let index = start;

    while (start1 <= end1 && start2 <= end2) {
        if (arr[start1] <= arr[start2]) {
            intermediate[index] = arr[start1];
            index++;
            start1++;
        } else if (arr[start2] < arr[start1]) {
            intermediate[index] = arr[start2];
            index++;
            start2++;
        }
    }
    //if partitioning was not even, or if one of the partition had more amount
    // of smaller elements than the other partition
    // copy remaining elements
    while (start1 <= end1) {
        intermediate[index] = arr[start1];
        start1++;
        index++;
    }

    while (start2 <= end2) {
        intermediate[index] = arr[start2];
        start2++;
        index++;
    }
    //now copy from intermediate back to array
    index = start;
    while (index <= end) {
        arr[index] = intermediate[index];
        index++;
    }
}

function drawQuickBars(start, end) {
    //erase the area
    control.clearRect(0, 0, 550, 1000)
    for (let i = 0; i < len_of_arr; i++) {
        control.fillStyle = "black";
        control.shadowOffsetX = 2;
        control.shadowColor = "chocolate";
        control.fillRect((widthOfEachBar + spaceBetweenBars) * i, 300 - qarr[i], widthOfEachBar, qarr[i]);
        if (qvisited[i]) {
            control.fillStyle = "#0006d13";
            control.fillRect((widthOfEachBar + spaceBetweenBars) * i, 300 - qarr[i], widthOfEachBar, qarr[i]);
            control.shadowOffsetX = 2;
        }
    }

    for (let i = start; i < end; i++) {
        control.fillStyle = "orange";
        control.fillRect((widthOfEachBar + spaceBetweenBars) * i, 300 - qarr[i], widthOfEachBar, qarr[i]);
        qvisited[i] = 1;
    }
    control.font = "30px Arial";
    control.fillStyle = "black";
    control.fillText("Quicksort", 180, 330);
}

function swap(data, i1, i2) {
    let temp = data[i1];
    data[i1] = data[i2];
    data[i2] = temp;
}

function partition(start, end) {
    var compare = end;
    var pivotPos = start;
    for (let i = start; i < end; i++) {
        if (qarr[i] <= qarr[compare]) {
            swap(qarr, i, pivotPos);
            pivotPos += 1;
        }
    }

    swap(qarr, pivotPos, compare);
    return pivotPos;
}

async function QuickSort(start, end) {
    if (start >= end) return;
    await sleep(100);
    drawQuickBars(start, end);
    pivot = partition(start, end);
    if (pivot >= len_of_arr) return;
    if (start <= pivot)
        await QuickSort(start, pivot - 1);
    if (pivot <= end)
        await QuickSort(pivot, end);
}

function drawMergeBars(start, end) {
    //erase the area
    control.clearRect(600, 0, 700, 1000)
    for (let i = 0; i < len_of_arr; i++) {
        control.fillStyle = "black";
        control.shadowOffsetX = 2;
        control.shadowColor = "chocolate";

        control.fillRect(600 + (widthOfEachBar + spaceBetweenBars) * i, 300 - arr[i], widthOfEachBar, arr[i]);
        // control.fillRect(600 + 12.5 * i, 300 - arr[i], 10, arr[i]);
        if (visited[i]) {
            control.fillStyle = "#0006d13";

            control.fillRect(600 + (widthOfEachBar + spaceBetweenBars) * i, 300 - arr[i], widthOfEachBar, arr[i]);
            control.shadowOffsetX = 2;
        }
    }

    for (let i = start; i < end; i++) {
        control.fillStyle = "orange";

        control.fillRect(600 + (widthOfEachBar + spaceBetweenBars) * i, 300 - arr[i], widthOfEachBar, arr[i]);
        visited[i] = 1;
    }

    control.font = "30px Arial";
    control.fillStyle = "black";
    control.fillText("MergeSort", 600 + 180, 330);
}

async function MergeSort(start, end) {
    if (start >= end) return;

    let partition = parseInt((start + end) / 2);
    await MergeSort(start, partition);
    await MergeSort(partition + 1, end);
    await merge(start, end);
    await drawMergeBars(start, end);

    await sleep(100);

}



function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

const drawInitialBars = async () => {
    // QuickSort(0, len_of_arr - 1);
    drawQuickBars();
    // MergeSort(0, len_of_arr - 1);
    drawMergeBars();

}


drawInitialBars();