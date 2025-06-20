        function navigate(select) {
          const value = select.value;
          if (value.startsWith('mailto:')) 
            {
            window.location.href = value;
          }
           else if (value.startsWith('#'))
             {
            window.location.hash = value;
          }
        }
      