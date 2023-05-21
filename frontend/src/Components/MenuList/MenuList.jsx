import s from "./MenuList.module.css";
import { Link } from "react-router-dom";

const MenuList = ({ menuItems }) => {
  return (
    <div className={s.menuList}>
      {menuItems.map((item) => (
        <Link to={`item/${item.id}`} key={menuItems.indexOf(item)} className={s.menuItemLink}>
          <MenuItem img={item.img} price={item.price} title={item.title} />
        </Link>
      ))}
    </div>
  );
};

export default MenuList;

const MenuItem = ({ img, title, price }) => {
  return (
    <div className={s.menuItem}>
      <img src={img} alt={title} />
      <h2 className={s.menuItemTitle}>{title}</h2>
      <div className={s.bottom}>
        <div>{`${price} ₽`}</div>
        <div className={s.arrow}>
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="6"
            height="10"
            viewBox="0 0 6 10"
            fill="none"
          >
            <path
              d="M1.45502 8.95998L4.71502 5.69998C5.10002 5.31498 5.10002 4.68498 4.71502 4.29998L1.45502 1.03998"
              stroke="white"
              strokeWidth="1.5"
              strokeMiterlimit="10"
              strokeLinecap="round"
              strokeLinejoin="round"
            />
          </svg>
        </div>
      </div>
    </div>
  );
};
