```mermaid
flowchart LR
    subgraph OnPrem[On-Prem（社内ネットワーク）]
        AD[Active Directory] -- TCP 389 --> Core[MNE移行管理サーバー]
        Domino[Domino サーバー] -- TCP 1352 --> Core
        Client[クライアント] -- TCP 139/445 --> Core
        Core -- TCP 1433 --> DB[(NME40DB)]
    end

    subgraph Cloud[Cloud]
        ExO[Exchange Online]
        Ex[Exchange]
    end

    Core -- TCP 443 --> ExO
    Core -- TCP 443 --> Ex
    Core -- TCP 80/443 --> Ex
