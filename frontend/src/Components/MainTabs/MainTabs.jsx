import Box from "@mui/material/Box";
import TabContext from "@mui/lab/TabContext";
import TabList from "@mui/lab/TabList";
import TabPanel from "@mui/lab/TabPanel";
import { useState } from "react";
import s from "./MainTabs.module.css";
import MenuList from "../MenuList/MenuList";
import coffeeImg from "../../assets/img/coffeeImg.png";

const MainTabs = () => {
  return (
    <div className={s.tabsWrapper}>
      <LabTabs />
    </div>
  );
};

const menuItemsMock = [
  { img: coffeeImg, title: "Капучино", price: 120 },
  {
    img: coffeeImg,
    title: "Капучино",
    price: 120,
  },
  { img: coffeeImg, title: "Капучино", price: 120 },
  { img: coffeeImg, title: "Капучино", price: 120 },
];

function LabTabs() {
  const [value, setValue] = useState("1");

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };

  return (
    <Box sx={{ width: "100%", typography: "body1" }}>
      <TabContext value={value}>
        <Box>
          <TabList onChange={handleChange} aria-label="lab API tabs example">
            <button className={s.tabButton} onClick={() => setValue("1")}>
              Топ недели
            </button>
            <button className={s.tabButton} onClick={() => setValue("2")}>
              Кофе
            </button>
            <button className={s.tabButton} onClick={() => setValue("3")}>
              Не кофе
            </button>
            <button className={s.tabButton} onClick={() => setValue("4")}>
              Еда
            </button>
            <button className={s.tabButton} onClick={() => setValue("5")}>
              Разное
            </button>
          </TabList>
        </Box>

        <div className={s.content}>
          <h1 className={s.contentTitle}>Лунго</h1>
          <button className="priceButton">120</button>
        </div>
        <TabPanel value="1">
          <MenuList menuItems={menuItemsMock} />
        </TabPanel>
        <TabPanel value="2">Item Two</TabPanel>
        <TabPanel value="3">Item Three</TabPanel>
        <TabPanel value="4">Item Three</TabPanel>
        <TabPanel value="5">Item Three</TabPanel>
      </TabContext>
    </Box>
  );
}

export default MainTabs;
