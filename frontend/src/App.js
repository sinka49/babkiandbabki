import "./App.css";
import * as React from "react";
import { useState } from "react";
import Header from "./Components/Header/Header";
import MainContent from "./Components/MainContent/MainContent";
import { HashRouter as Router, Route, Routes } from "react-router-dom";
import MenuList from "./Components/MenuList/MenuList";
import coffeeImg from "./assets/img/coffeeImg.png";
import CoffeeCard from "./Components/CoffeeCard/CoffeeCard";
import Order from "./Components/Order/Order";

const menuItemsMock = [
  { img: coffeeImg, title: "Капучино", price: 120, id: 1 },
  {
    img: coffeeImg,
    title: "Капучино",
    price: 120,
    id: 2,
  },
  { img: coffeeImg, title: "Латте", price: 120, id: 3 },
  { img: coffeeImg, title: "Американо", price: 120, id: 4 },
  { img: coffeeImg, title: "Эспрессо", price: 120, id: 5 },
  { img: coffeeImg, title: "Капучино", price: 120, id: 6 },
  { img: coffeeImg, title: "Флет Уайт", price: 120, id: 7 },
  { img: coffeeImg, title: "Капучино", price: 120, id: 8 },
  { img: coffeeImg, title: "Капучино", price: 120, id: 9 },
];

function App() {
  const [isOrderOpen, setIsOrderOpen] = useState(false);

  return (
    <Router>
      <div className={"App"}>
        <Routes>
          <Route
            path="/"
            element={
              <>
                <Header />
                <div className="wrapper">
                  <MainContent />
                  <MenuList menuItems={menuItemsMock} />
                  <button
                    className="orderButton"
                    onClick={() => setIsOrderOpen(true)}
                  >
                    Ваш заказ
                  </button>
                </div>
              </>
            }
          />
          <Route path="/item/:id" element={<CoffeeCard />} />
        </Routes>
        <Order isOpen={isOrderOpen} setIsOrderOpen={setIsOrderOpen} />
      </div>
    </Router>
  );
}

export default App;
