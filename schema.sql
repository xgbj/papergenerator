drop table if exists paper;
create table paper (
  alias text not null,
  papername text not null,
  `number` integer not null,
  type integer not null,
  content text not null,
  optiona text,
  optionb text,
  optionc text,
  optiond text,
  answer text not null
);