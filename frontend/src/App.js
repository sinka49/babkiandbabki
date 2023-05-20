import "./App.css";
import Header from "./Components/Header/Header";
import MainComponent from "./Components/Main/MainComponent";
import { pink } from "@mui/material/colors";
import { createTheme, ThemeProvider } from "@mui/material";

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
        {/*<Header />*/}
        <MainComponent theme={theme} />
      </div>
    </ThemeProvider>
  );
}

export default App;
