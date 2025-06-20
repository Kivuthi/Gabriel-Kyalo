function navigate(selectElement) {
    const url = selectElement.value;
    if (url) {
      window.location.href = url;
    }
  }

  function navigate(selectElement) {
    const url = selectElement.value;
    if (url) {
      window.location.href = url;
      selectElement.selectedIndex = 0; 
    }
  }
  