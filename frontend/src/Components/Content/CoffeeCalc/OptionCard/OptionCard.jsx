import s from "./OptionCard.module.css";

export const OptionCard = ({ name }) => {
  return <div className={s.wrapper}>{name}</div>;
};
