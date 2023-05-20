import s from "./CoffeeCalc.module.css";
import NavigateBeforeIcon from "@mui/icons-material/NavigateBefore";
import IconButton from "@mui/material/IconButton";
import InfoIcon from "@mui/icons-material/Info";
import coffee from "../../../assets/img/coffee.webp";
import * as React from "react";
import Tabs from "@mui/material/Tabs";
import Tab from "@mui/material/Tab";
import Box from "@mui/material/Box";

export const CoffeeCalc = () => {
  return (
    <div className={s.wrapper}>
      <div className={s.cardHeader}>
        <IconButton aria-label="delete">
          <NavigateBeforeIcon fontSize="large" />
        </IconButton>
        <IconButton aria-label="delete">
          <InfoIcon fontSize="medium" />
        </IconButton>
      </div>
      <div className={s.coffeeCard}>
        <div className={s.imageContainer}>
          <img src={coffee} alt="coffee" className={s.coffeeImage} />
        </div>
        <h1 className={s.title}>Капучино</h1>
        <p className={s.description}>Классический кофе с молочной пенкой</p>
        <ColorTabs />
      </div>
    </div>
  );
};

export default CoffeeCalc;

function ColorTabs() {
  const [value, setValue] = React.useState("one");

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };

  return (
    <Box sx={{ width: "100%" }}>
      <Tabs
        value={value}
        onChange={handleChange}
        textColor="secondary"
        indicatorColor="secondary"
        aria-label="secondary tabs example"
        sx={{}}
      >
        <Tab value="one" label="Item One" />
        <Tab value="two" label="Item Two" />
        <Tab value="three" label="Item Three" />
      </Tabs>
    </Box>
  );
}
