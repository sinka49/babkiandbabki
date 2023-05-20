import s from "./MenuList.module.css";

const MenuList = ({ menuItems }) => {
  return (
    <div className={s.menuList}>
      {menuItems.map((item) => (
        <MenuItem
          img={item.img}
          price={item.price}
          title={item.title}
          key={menuItems.indexOf(item)}
        />
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
      <div>{`${price} ₽`}</div>
    </div>
  );
};
