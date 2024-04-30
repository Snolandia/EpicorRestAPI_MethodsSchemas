import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.PartLotIncludeAttributesSvc
// Description: PartLotDynAttrValueSetView Business Object
// Version: v1
*/ 



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// OData methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => application/json
   */  
export function getServiceDocument(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<JSON>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartLotIncludeAttributesSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as JSON)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: Returns metadata document => content
   */  
export function get_metadata(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartLotIncludeAttributesSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// Custom methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Invoke method GetRowsLotTracker
   OperationID: GetRowsLotTracker
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRowsLotTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsLotTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsLotTracker(requestBody:GetRowsLotTracker_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRowsLotTracker_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartLotIncludeAttributesSvc/GetRowsLotTracker", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetRowsLotTracker_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// OData Schemas:
//////////////////////////////////////////////////////////////////////////



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
export interface Erp_Tablesets_PartLotDynAttrValueSetViewRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The PartNum field identifies the Part.  */  
   PartNum:string,
      /**  Unique lot number for the part.  */  
   LotNum:string,
      /**  Optional lot number description.  */  
   PartLotDescription:string,
      /**  Indicates that there is still some of the lot on hand.  */  
   OnHand:boolean,
      /**  Earliest date that the lot was referenced.  */  
   FirstRefDate:string,
      /**  Latest date that the lot was referenced.  */  
   LastRefDate:string,
      /**   Used only when costing method is by lot. Average Unit Labor Cost of the Part.  It is directly updated by by  Manufacture receipts, Bill of Material cost rollup, Purchase Part receipts or cost adjustment program.  Basically when updating an average cost the following logic is used.
 NEW AVG COST = ((ONHAND QTY * AVG COST) + TOTAL RECPT COST) / (ONHAND QTY + RECPT QTY).  Exceptions to this formula are if the onhand qty begins as a negative, then its value is not included in the calculations.  If the receipt transaction is of negative value then the average cost will not be changed.
GENERAL NOTES ABOUT UNIT COSTS:
The unit cost fields in the Part record are used as default cost in job material detail. The system is configurable to use either Average, Standard or Last unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during receipt entry regardless of the Costing method specified.  */  
   LotLaborCost:number,
      /**  Used only for lot costing method. Average burden unit cost. This is updated by Manufactured receipt process, Purchased Part Receipt and inventory adjustment programs.  See the description in the LaborCost for the formula for calculating average unit costs.  */  
   LotBurdenCost:number,
      /**  Used only for costing by lot.  Average Material Unit cost.  maintained Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See LotLaborCost description for explanation of updating with the receipts cost.  */  
   LotMaterialCost:number,
      /**  Used only when costing by lot. Subcontract Unit cost. Indirectly maintained by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the AvgLaborCost description for explanation of updating with the receipts cost.  */  
   LotSubContCost:number,
      /**  Use only when lot t cosintg methid is used. Lot  Material Burden Unit cost. Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the AvgLaborCost description for explanation of updating with the receipts cost.  */  
   LotMtlBurCost:number,
      /**  Determined by setting on Part.AttExpDt if required or tracked.  */  
   ExpirationDate:string,
      /**  Required Shipping  Documents Available.A flag manually set by the user to indicate that the required documents for the Part/Lot are available. In order to set to Yes, at least one attachment having a DocType with Shipment = yes must exist for the Part/Lot.  If the Part.ShipDocReq = yes  then PartLot.ShipDocsA vail must = yes before the system will allow shipment of the Part/LotRequires DocManagement license.  */  
   ShipDocAvail:boolean,
      /**  Determined by setting on Part.AttBatch if required or tracked.  */  
   Batch:string,
      /**  Determined by setting on Part.AttMfgBatch if required or tracked.  */  
   MfgBatch:string,
      /**  Determined by setting on Part.AttMfgLot if required or tracked.  */  
   MfgLot:string,
      /**  Determined by setting on Part.AttHeat if required or tracked.  */  
   HeatNum:string,
      /**  Determined by setting on Part.AttFirmware if required or tracked.  */  
   FirmWare:string,
      /**  Determined by setting on Part.AttBeforeDt if required or tracked.  */  
   BestBeforeDt:string,
      /**  Determined by setting on Part.AttMfgDt if required or tracked.  */  
   MfgDt:string,
      /**  Determined by setting on Part.AttCureDt if required or tracked.  */  
   CureDt:string,
      /**  Expire Date  */  
   ExpireDt:string,
      /**   Used only when costing method is by LOT FIFO. FIFO Average Unit Labor Cost of the Part per Lot.  It is directly updated by by  Manufacture receipts, Bill of Material cost rollup, Purchase Part receipts or cost adjustment program.  Basically when updating a FIFO lot average cost the following logic is used.
 NEW AVG COST = sum of all (FIFO OnHandQty * FIFO costs)
GENERAL NOTES ABOUT UNIT COSTS:
The unit cost fields in the PartCost record are used as default cost in job material detail. The system is configurable to use either Average, Standard, Last or FIFO unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during receipt entry regardless of the Costing method specified.  */  
   FIFOLotLaborCost:number,
      /**  Used only for lot FIFO costing method. FIFO Average burden unit cost. This is updated by Manufactured receipt process, Purchased Part Receipt and inventory adjustment programs.  See the description in the FIFOLotLaborCost for the formula for calculating average unit costs.  */  
   FIFOLotBurdenCost:number,
      /**  Used only for costing by lot FIFO.  FIFO Average Material Unit cost maintained indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See FIFOLotLaborCost description for explanation of updating with the receipts cost.  */  
   FIFOLotMaterialCost:number,
      /**  Used only when costing by lot FIFO. FIFO Average Subcontract Unit cost. Indirectly maintained by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the FIFOLotLaborCost description for explanation of updating with the receipts cost.  */  
   FIFOLotSubContCost:number,
      /**  Use only when lot FIFO costing method is used. FIFO Lot Average Material Burden Unit cost maintained indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the FIFOLotLaborCost description for explanation of updating with the receipts cost.  */  
   FIFOLotMtlBurCost:number,
      /**   Malaysia Localization
LMW Commissioner of Oath's Number  */  
   CSFLMWComOath:string,
      /**   Malaysia Localization
CJ5 Form Number  */  
   CSFCJ5FormNbr:string,
      /**   Malaysia Localization
CJ5 Vessel Number  */  
   CSFCJ5Vessel:string,
      /**   Malaysia Localization
The start date of CJ5 approved period  */  
   CSFCJ5ApvlStart:string,
      /**   Malaysia Localization
The end date of CJ5 approved period  */  
   CSFCJ5ApvlEnd:string,
      /**  Stores the number of the import document.  */  
   ImportNum:string,
      /**  Stores the Country from which the document is imported.  */  
   ImportedFrom:number,
      /**  Location description from which the document is imported.  */  
   ImportedFromDesc:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  MXImportLocation  */  
   MXImportLocation:string,
      /**  MXImportDate  */  
   MXImportDate:string,
      /**  Total OnHand Quantity used specific for Average Costing calculations  */  
   TotalQtyAvg:number,
      /**  Country number of the Origin Country (defaults from Part Country of Origin).  */  
   ISOrigCountryNum:number,
      /**  AttributeSetID associated with the Part  */  
   DynAttrValueSetAttributeSetID:number,
      /**  Description of Attribute Set  */  
   DynAttrValueSetDescription:string,
      /**  Revision Num associated with this Part  */  
   DynAttrValueSetRevisionNum:string,
      /**  Attribute Set's short description  */  
   DynAttrValueSetShortDescription:string,
      /**  Total OnhandQty from all bins  */  
   PartBinOnhandQty:number,
      /**  Attribute Class ID associated with the Part  */  
   PartNumAttrClassID:string,
      /**  IUM associated with Part number  */  
   PartNumIUM:string,
      /**  SalesUM associated with Part number  */  
   PartNumSalesUM:string,
   ScrLotBurdenCost:number,
   ScrLotLaborCost:number,
   ScrLotMaterialCost:number,
   ScrLotMtlBurCost:number,
   ScrLotSubContCost:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartLotDynAttrValueSetViewTableset{
   PartLotDynAttrValueSetView:Erp_Tablesets_PartLotDynAttrValueSetViewRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsLotTracker_input{
   whereClause:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRowsLotTracker_output{
   returnObj:Erp_Tablesets_PartLotDynAttrValueSetViewTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

export interface Ice_Extensions_ExtensionRow{
   ColumnValues:object
   RowMod:string,
   SysRowID:string,
}

export interface Ice_Extensions_ExtensionTableColumn{
   ColumnName:string,
   ColumnType:string,
}

export interface Ice_Extensions_ExtensionTableData{
   Table:Ice_Extensions_ExtensionRow[],
   SystemCode:string,
   TableName:string,
   Columns:Ice_Extensions_ExtensionTableColumn[],
   PrimaryKeyColumns:string,
   PeerTableSystemCode:string,
   PeerTableName:string,
}

