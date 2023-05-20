import "./App.css";
import { pink } from "@mui/material/colors";
import { createTheme, ThemeProvider } from "@mui/material";
import CoffeeCalc from "./Components/Content/CoffeeCalc/CoffeeCalc";

const theme = createTheme({
  palette: {
    primary: {
      main: pink[300],
    },
  },
});

function App() {
  return (
    <ThemeProvider theme={theme}>
      <div className="App">
        <CoffeeCalc />
      </div>
    </ThemeProvider>
  );
}

export default App;
