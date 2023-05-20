import s from "./MainContent.module.css";

const MainContent = () => {
  return (
    <div className={s.mainContent}>
      <h1 className={s.contentTitle}>Лунго</h1>
      <button className="priceButton">120</button>
    </div>
  );
};

export default MainContent;
