import s from "./Header.module.css";
import { Link } from "react-router-dom";

const optionsMock = [
  "Топ недели",
  "Кофе",
  "Не кофе",
  "Уда",
  "Десерты",
  "Разное",
];

const Header = () => {
  return (
    <header className={s.header}>
      <div className={s.headerTop}>
        <button className={s.headerButton}>
          Войти
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="16"
            height="16"
            viewBox="0 0 16 16"
            fill="none"
          >
            <path
              fillRule="evenodd"
              clipRule="evenodd"
              d="M8 0.5C3.86 0.5 0.5 3.86 0.5 8C0.5 12.14 3.86 15.5 8 15.5C12.14 15.5 15.5 12.14 15.5 8C15.5 3.86 12.14 0.5 8 0.5ZM12.77 11.6225C11.6975 10.3175 9.095 9.875 8 9.875C6.905 9.875 4.3025 10.3175 3.23 11.6225C2.465 10.6175 2 9.365 2 8C2 4.6925 4.6925 2 8 2C11.3075 2 14 4.6925 14 8C14 9.365 13.535 10.6175 12.77 11.6225ZM5.375 6.125C5.375 4.67 6.545 3.5 8 3.5C9.455 3.5 10.625 4.67 10.625 6.125C10.625 7.58 9.455 8.75 8 8.75C6.545 8.75 5.375 7.58 5.375 6.125Z"
              fill="white"
            />
          </svg>
        </button>
      </div>
      <nav className={s.navigation}>
        {optionsMock.map((item) => (
          <Link to="#" key={optionsMock.indexOf(item)} className={s.navLink}>
            <button className={s.navButton}>{item}</button>
          </Link>
        ))}
      </nav>
    </header>
  );
};

export default Header;
