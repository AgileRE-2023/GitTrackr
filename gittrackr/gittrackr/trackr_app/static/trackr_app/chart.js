const bar = document.getElementById('repo').getContext('2d');
const canvas1 = document.getElementById('repo');
const ChartOptions = {
  plugins: {  
    legend: {
      labels: {
        color: "blue",  
        font: {
          size: 18 
        }
      }
    }
  },
  scales: {
    y: {  
      ticks: {
        color: "green", 
        font: {
          size: 18, 
        },
        stepSize: 1,
        beginAtZero: true
      }
    },
    x: { 
      ticks: {
        color: "purple",  
        font: {
          size: 14 
        },
        stepSize: 1,
        beginAtZero: true
      }
    }
  }
};



  var Cont1 = {
    label: 'Airlangga',
    data: 
     [1,2,1,4,3,4,1,3,0],
    borderColor: 'white',
    fill: false,
    borderJoinStyle: 'miter',
    tension: 0
  }
  var Cont2 = {
    label: 'Aivel',
    data: 
     [1,2,1,2,3,0,1,3,0],
    borderColor: 'red',
    fill: false,
    borderJoinStyle: 'miter',
    tension: 0
  }
  var Cont3 = {
    label: 'Rayhan',
    data: 
     [1,2,4,3,2,1,2,2,3],
    borderColor: 'green',
    fill: false,
    borderJoinStyle: 'miter',
    tension: 0
  }
  const chart = new Chart(bar,   {
    type: 'line',
    data: {
      labels: [1,2,3,4,5,6,7,8,9],  
      datasets: [Cont1,Cont2,Cont3],
    },
    options: ChartOptions
  });
