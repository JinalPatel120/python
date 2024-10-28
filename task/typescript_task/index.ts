// const car: { type: string, model: string, year: number } = {
//     type: "Toyota",
//     model: "Corolla",
//     year: 2009
//   };


  interface Car{
    type:string,
    model:string,
    year:number
  }
  const car:Car = {
    type: "Toyota",
    model: "Corolla",
    year: "jisdn" as any
  };



  