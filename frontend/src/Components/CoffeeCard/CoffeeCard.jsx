import s from "./CoffeeCard.module.css";
import card from "../../assets/img/card.png";
import * as React from "react";
import { useState } from "react";
import Tabs from "@mui/material/Tabs";
import Tab from "@mui/material/Tab";
import Box from "@mui/material/Box";
import { Link } from "react-router-dom";
import cn from "classnames";

const CoffeeCard = () => {
  const [value, setValue] = React.useState("two");
  const [showMenu, setShowMenu] = useState(0);

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };

  const optionsContent = (id) => {
    switch (id) {
      case 1:
        return ["Овсяное", "Миндальное", "Кокосовое", "Банановое"];
      case 2:
        return ["Карамель", "Орех", "Ваниль", "Мята"];
      case 3:
        return ["Стандартная", "Погорячее"];
      case 4:
        return ["Сахар", "Подставка", "Приборы", "Без крышки"];
    }
  };

  return (
    <div className={s.cardWrapper}>
      <div className={s.header}>
        <Link to="/">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="22"
            height="22"
            viewBox="0 0 22 22"
            fill="none"
          >
            <path
              d="M8.14214 13.799L13.799 8.14215M13.799 13.799L8.14214 8.14215M18.0416 18.0416C21.9307 14.1526 21.9307 7.7886 18.0416 3.89951C14.1525 0.0104261 7.78859 0.0104261 3.8995 3.89951C0.0104106 7.7886 0.0104106 14.1526 3.8995 18.0416C7.78859 21.9307 14.1525 21.9307 18.0416 18.0416Z"
              stroke="#ADADAD"
              strokeWidth="1.5"
              strokeLinecap="round"
              strokeLinejoin="round"
            />
          </svg>
        </Link>
      </div>
      <img src={card} alt="coffee" className={s.img} />
      <h1 className={s.title}>Капучино</h1>
      <p className={s.description}>Классический кофе с молочной пенкой</p>

      <Box sx={{ width: "100%" }}>
        <Tabs
          value={value}
          onChange={handleChange}
          textColor="secondary"
          indicatorColor="secondary"
          centered
        >
          <Tab value="one" label="200 мл" />
          <Tab value="two" label="300 мл" />
          <Tab value="three" label="400 мл" />
        </Tabs>
      </Box>

      <div className={s.buttons}>
        <button className={s.optionButton} onClick={() => setShowMenu(1)}>
          Молоко
        </button>
        <button className={s.optionButton} onClick={() => setShowMenu(2)}>
          {" "}
          Сироп{" "}
        </button>
        <button className={s.optionButton} onClick={() => setShowMenu(3)}>
          Температура
        </button>
        <button className={s.optionButton} onClick={() => setShowMenu(4)}>
          Кофе с собой
        </button>
      </div>

      <div className={s.bottom}>
        <button className={s.orderButton}>
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="24"
            height="24"
            viewBox="0 0 24 24"
            fill="none"
          >
            <path
              d="M8.5 14.25C8.5 16.17 10.08 17.75 12 17.75C13.92 17.75 15.5 16.17 15.5 14.25M8.81 2L5.19 5.63M15.19 2L18.81 5.63"
              stroke="black"
              strokeWidth="1.5"
              strokeMiterlimit="10"
              strokeLinecap="round"
              strokeLinejoin="round"
            />
            <path
              d="M2 7.8501C2 6.0001 2.99 5.8501 4.22 5.8501H19.78C21.01 5.8501 22 6.0001 22 7.8501C22 10.0001 21.01 9.8501 19.78 9.8501H4.22C2.99 9.8501 2 10.0001 2 7.8501Z"
              stroke="black"
              strokeWidth="1.5"
            />
            <path
              d="M3.5 10L4.91 18.64C5.23 20.58 6 22 8.86 22H14.89C18 22 18.46 20.64 18.82 18.76L20.5 10"
              stroke="black"
              strokeWidth="1.5"
              strokeLinecap="round"
            />
          </svg>
          120 ₽
        </button>
      </div>

      <div
        className={cn(s.optionMenu, showMenu ? s.menuShowed : "")}
        onClick={() => setShowMenu(false)}
      >
        <div className={s.buttons}>
          {optionsContent(showMenu)?.map((item) => (
            <button
              className={s.optionButton}
              style={{ backgroundColor: "#FFFFFF" }}
              onClick={() => setShowMenu(0)}
            >
              {item}
            </button>
          ))}
        </div>
      </div>
    </div>
  );
};

export default CoffeeCard;
