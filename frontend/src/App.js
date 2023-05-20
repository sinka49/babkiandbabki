import "./App.css";
import * as React from "react";
import Header from "./Components/Header/Header";
import MainContent from "./Components/MainContent/MainContent";
import { BrowserRouter } from "react-router-dom";
import MenuList from "./Components/MenuList/MenuList";
import coffeeImg from "./assets/img/coffeeImg.png";

const menuItemsMock = [
  { img: coffeeImg, title: "Капучино", price: 120 },
  {
    img: coffeeImg,
    title: "Капучино",
    price: 120,
  },
  { img: coffeeImg, title: "Капучино", price: 120 },
  { img: coffeeImg, title: "Капучино", price: 120 },
  { img: coffeeImg, title: "Капучино", price: 120 },
  { img: coffeeImg, title: "Капучино", price: 120 },
  { img: coffeeImg, title: "Капучино", price: 120 },
  { img: coffeeImg, title: "Капучино", price: 120 },
  { img: coffeeImg, title: "Капучино", price: 120 },
  { img: coffeeImg, title: "Капучино", price: 120 },
  { img: coffeeImg, title: "Капучино", price: 120 },
  { img: coffeeImg, title: "Капучино", price: 120 },
  { img: coffeeImg, title: "Капучино", price: 120 },
  { img: coffeeImg, title: "Капучино", price: 120 },
  { img: coffeeImg, title: "Капучино", price: 120 },
  { img: coffeeImg, title: "Капучино", price: 120 },
];
function App() {
  return (
    <BrowserRouter>
      <div className={"App"}>
        <Header />
        <div className="wrapper">
          <MainContent />
          <MenuList menuItems={menuItemsMock} />
          <button className="orderButton">ваш заказ</button>
        </div>
      </div>
    </BrowserRouter>
  );
}

export default App;
