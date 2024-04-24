import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.CapPromiseSvc
// Description: bo/CapPromise/CapPromise.p
           Capable To Promise business object
           smr
           07/15/04
// Version: v1



//////////////////////////////////////////////////////////////////////////
// OData methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CapPromiseSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CapPromiseSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
// Custom methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Invoke method CalculateCTP
   Description: Performs the calculation logic for CTP.
Before calling this method all CapPromiseDtl records must have the RowMod
field set to 'U'.
   OperationID: CalculateCTP
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalculateCTP_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalculateCTP_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CalculateCTP(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CapPromiseSvc/CalculateCTP", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CancelCTP
   Description: Performs the cancellation of CTP.
Before calling this method all CapPromiseDtl records must have the RowMod
field set to 'U'.
   OperationID: CancelCTP
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CancelCTP_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CancelCTP_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CancelCTP(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CapPromiseSvc/CancelCTP", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CapPromiseDmdGetNew
   Description: Creates a temporary record to store information needed for the
Capable To Promise process.
   OperationID: CapPromiseDmdGetNew
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CapPromiseDmdGetNew_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CapPromiseDmdGetNew_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CapPromiseDmdGetNew(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CapPromiseSvc/CapPromiseDmdGetNew", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CapPromiseGetNew
   Description: Creates a temporary record to store information needed for the
Capable To Promise process.
   OperationID: CapPromiseGetNew
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CapPromiseGetNew_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CapPromiseGetNew_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CapPromiseGetNew(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CapPromiseSvc/CapPromiseGetNew", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeCapPromiseDtlFiniteSchedule
   Description: Reassigns the OverrideMtlConstraints and EnableOverrideMtlConstraints
fields based on the value of FiniteSchedule.
   OperationID: ChangeCapPromiseDtlFiniteSchedule
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCapPromiseDtlFiniteSchedule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCapPromiseDtlFiniteSchedule_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCapPromiseDtlFiniteSchedule(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CapPromiseSvc/ChangeCapPromiseDtlFiniteSchedule", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeCapPromiseGlobalCTP
   Description: Updates CapPromiseDtl records based on the new value of CapPromise.GlobalCTP.
Before calling this method all CapPromiseDtl records must have the RowMod
field set to 'U'.
   OperationID: ChangeCapPromiseGlobalCTP
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCapPromiseGlobalCTP_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCapPromiseGlobalCTP_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCapPromiseGlobalCTP(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CapPromiseSvc/ChangeCapPromiseGlobalCTP", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeCapPromiseProjectedStartDate
   Description: Updates CapPromiseDtl records based on the new value of
CapPromise.ProjectedStartDate.
Before calling this method all CapPromiseDtl records must have the RowMod
field set to 'U'.
   OperationID: ChangeCapPromiseProjectedStartDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCapPromiseProjectedStartDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCapPromiseProjectedStartDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCapPromiseProjectedStartDate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CapPromiseSvc/ChangeCapPromiseProjectedStartDate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ConfirmCTP
   Description: Performs the confirmation logic for CTP.
Before calling this method all CapPromiseDtl records must have the RowMod
field set to 'U'.
   OperationID: ConfirmCTP
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ConfirmCTP_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ConfirmCTP_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ConfirmCTP(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CapPromiseSvc/ConfirmCTP", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ConfirmCTPPOSug
   Description: Performs the confirmation logic for the PO Suggestion created for CTP.
   OperationID: ConfirmCTPPOSug
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ConfirmCTPPOSug_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ConfirmCTPPOSug_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ConfirmCTPPOSug(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CapPromiseSvc/ConfirmCTPPOSug", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method deleteJob
   Description: Purpose:     Delete the CTP job and leave the results from the calculation when parameter
from Site Configuration is set as "N - No Job"
Parameters:  none
Notes:       First the temporal job "CTP Job" is deleted and then as we alraedy have save the results from
CTP calculation into the ttCapPromise ds, we just update the OrderDtl and OrderRel records.
DEVELOPER NOTE: this method is also called from OM\ProcessDemand.cs and will require changes there if the parameters are changed.
   OperationID: deleteJob
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/deleteJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_deleteJob(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CapPromiseSvc/deleteJob", {
          method: 'post',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DoWhseAtp
   OperationID: DoWhseAtp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DoWhseAtp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DoWhseAtp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DoWhseAtp(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CapPromiseSvc/DoWhseAtp", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method FindMaxConv
   Description: Purpose:  Find the maximum convertable quantity for giving unit of measure and quantity
   OperationID: FindMaxConv
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FindMaxConv_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FindMaxConv_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FindMaxConv(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CapPromiseSvc/FindMaxConv", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetOrderPromiseDate
   Description: Sets the completion date for all detail records based on the latest date
of the detail records.
Before calling this method all CapPromiseDtl records must have the RowMod
field set to 'U'.
   OperationID: SetOrderPromiseDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetOrderPromiseDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetOrderPromiseDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetOrderPromiseDate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CapPromiseSvc/SetOrderPromiseDate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
// OData Schemas:
//////////////////////////////////////////////////////////////////////////



//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param lDemandEntry
      @param ds
   */  
export interface CalculateCTP_input{
      /**  If comes from Demand Entry or not.  */  
   lDemandEntry:boolean,
   ds:Erp_Tablesets_CapPromiseTableset[],
}

export interface CalculateCTP_output{
parameters : {
      /**  output parameters  */  
   outMessage:string,
   ds:Erp_Tablesets_CapPromiseTableset[],
}
}

   /** Required : 
      @param lDemandEntry
      @param ds
   */  
export interface CancelCTP_input{
   lDemandEntry:boolean,
   ds:Erp_Tablesets_CapPromiseTableset[],
}

export interface CancelCTP_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CapPromiseTableset[],
}
}

   /** Required : 
      @param DemandContractNum
      @param DemandHeadSeq
      @param DemandDtlSeq
      @param DemandScheduleSeq
   */  
export interface CapPromiseDmdGetNew_input{
      /**  The Demand Contract number for the process  */  
   DemandContractNum:number,
      /**  The Demand Head Sequence for the process  */  
   DemandHeadSeq:number,
      /**  The Demand Detail Sequence for the process  */  
   DemandDtlSeq:number,
      /**  The Demand Schedule Sequence number for the process  */  
   DemandScheduleSeq:number,
}

export interface CapPromiseDmdGetNew_output{
   returnObj:Erp_Tablesets_CapPromiseTableset[],
}

   /** Required : 
      @param OrderNum
   */  
export interface CapPromiseGetNew_input{
      /**  The order number for the process  */  
   OrderNum:number,
}

export interface CapPromiseGetNew_output{
   returnObj:Erp_Tablesets_CapPromiseTableset[],
}

   /** Required : 
      @param ProposedFiniteSchedule
      @param OrderNum
      @param OrderLine
      @param OrderRelNum
      @param ds
   */  
export interface ChangeCapPromiseDtlFiniteSchedule_input{
      /**  The proposed value for FiniteSchedule  */  
   ProposedFiniteSchedule:boolean,
      /**  The Order Number  */  
   OrderNum:number,
      /**  The Order Line  */  
   OrderLine:number,
      /**  The Order Release Number  */  
   OrderRelNum:number,
   ds:Erp_Tablesets_CapPromiseTableset[],
}

export interface ChangeCapPromiseDtlFiniteSchedule_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CapPromiseTableset[],
}
}

   /** Required : 
      @param ProposedGlobalCTP
      @param ds
   */  
export interface ChangeCapPromiseGlobalCTP_input{
      /**  The proposed value for GlobalCTP  */  
   ProposedGlobalCTP:boolean,
   ds:Erp_Tablesets_CapPromiseTableset[],
}

export interface ChangeCapPromiseGlobalCTP_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CapPromiseTableset[],
}
}

   /** Required : 
      @param ProposedProjectedStartDate
      @param ds
   */  
export interface ChangeCapPromiseProjectedStartDate_input{
      /**  The proposed value for ProjectedStartDate  */  
   ProposedProjectedStartDate:string,
   ds:Erp_Tablesets_CapPromiseTableset[],
}

export interface ChangeCapPromiseProjectedStartDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CapPromiseTableset[],
}
}

   /** Required : 
      @param iSugNum
   */  
export interface ConfirmCTPPOSug_input{
      /**  PO Suggestion Number to be confirmed.  */  
   iSugNum:number,
}

export interface ConfirmCTPPOSug_output{
parameters : {
      /**  output parameters  */  
   opError:string,
}
}

   /** Required : 
      @param ds
   */  
export interface ConfirmCTP_input{
   ds:Erp_Tablesets_CapPromiseTableset[],
}

export interface ConfirmCTP_output{
parameters : {
      /**  output parameters  */  
   opError:string,
   ds:Erp_Tablesets_CapPromiseTableset[],
}
}

   /** Required : 
      @param atpdate
      @param atpWhseqty
      @param ipPast
   */  
export interface DoWhseAtp_input{
   atpdate:string,
   atpWhseqty:number,
   ipPast:boolean,
}

export interface DoWhseAtp_output{
parameters : {
      /**  output parameters  */  
   atpdate:string,
   atpWhseqty:number,
}
}

export interface Erp_Tablesets_CapPromiseDtlRow{
   Company:string,
   OrderNum:number,
   OrderLine:number,
   OrderRelNum:number,
   PartNum:string,
   LineDesc:string,
      /**  Quantity displayed in base UOM  */  
   Quantity:number,
   NeedByDate:string,
   ProposedStartDate:string,
   CTP:boolean,
   EnableCTP:boolean,
      /**  The calculated completion date.  */  
   CalculatedCompDate:string,
      /**  The user entered completion date.  Defaults from CalculatedCompDate.  */  
   UserCompDate:string,
   Confirm:boolean,
   EnableConfirm:boolean,
   JobNum:string,
   ErrorText:string,
   FiniteSchedule:boolean,
   OverrideMtlConstraints:boolean,
   EnableOverrideMtlConstraints:boolean,
   HasBeenConfirmed:boolean,
   NewOrderRelNum:number,
      /**  Describes if this record comes from a kit component (C) or a kit parent (P), and is blank if it's a non-kit line  */  
   KitFlag:string,
      /**  If this record comes from a kit part then this field will hold the parent line number for this component. If the record comes from the kit parent then this field will hold the same value as the OrderLine  */  
   KitParentLine:number,
      /**  The quantity per kit in case that this line comes from a kit component, if not it will be 0  */  
   KitQtyPer:number,
      /**  On Hand Qty for the record's PartNum, this is the sum of all PartBin for this part and it calculated on the CapPromiseGetNew  */  
   OnHandQty:number,
      /**  HasChangedData  */  
   HasChangedData:boolean,
   QuantityUOM:string,
      /**  Quantity displayed in selling UOM  */  
   SellingQuantity:number,
      /**  Selling Quantity UOM  */  
   SellingQuantityUOM:string,
      /**  Buy To Order flag of the OrderRel  */  
   BuyToOrder:boolean,
   SugNum:number,
      /**  Demand Contract Number  */  
   DemandContractNum:number,
      /**  Demand Head sequence  */  
   DemandHeadSeq:number,
      /**  Demand Detail Sequence  */  
   DemandDtlSeq:number,
      /**  DemandScheduleSeq  */  
   DemandScheduleSeq:number,
   NewDemandScheduleSeq:number,
   MultiLevelCTP:boolean,
   EnableMultiLevelCTP:boolean,
      /**  This column will be calculated as the Ship by date plus the delivery days.  */  
   CTPNeedByDate:string,
      /**  This column will be calculated as the Completion date plus customer periodicity logic.  */  
   CTPShipDate:string,
      /**  Use by CTP from Demand Entry, indicates for each schedule if the Job created for CTP will be firmed and the PO Sug will create a PO after the schedule is processed and a order release is now available.  */  
   ConfirmAll:boolean,
   ContractID:string,
   LinkToContract:boolean,
      /**  Will show the OrderRel.ReqDate or DemandSchedule.ReqDate (ship by Date).  */  
   ReqDate:string,
      /**  True = the calculated CTP date will not meet the Ship By date on the order line/release  */  
   ReqDteNotMet:boolean,
      /**  A numerical value in days to signify by how many days the calculated date misses or is greater than the Ship By date  */  
   ReqDteMissedByDays:number,
      /**  The plant from either OrderRel.Plant or DemandSchedule.Plant depending on the source of the CTP used to calculate the difference between the calculated completion date and the ship by date after all dates have been calculated for the CapPromiseDtl  */  
   Plant:string,
      /**  The inventory quantity that is projected to be available on the requested ship date and is not already committed to a demand as of when the CTP calculation is being done (today).  */  
   AvailQty:number,
      /**  Holds the CTP job number or translated text for the values of CapPromiseDtl.JobNum: stock, OK - Stock, Lead time, PO Suggestion, etc  */  
   JobNumDisp:string,
      /**  The column is only populated if Customer/ShipTo Demand Update Date (DemandCapPromisDate) = true. it is used to determne how to set the dates for a new DemandSchedule split line during Confirm CTP  */  
   DemandCapPromiseUpdate:string,
      /**  Indicates whether the demand schedule is for a drop ship part.  */  
   IsDropShip:boolean,
      /**  Date that was calculated for the completion of this kit component. After all CTP calcs the kit components will all be changed to the latest date calculated for any component on the kit.  */  
   KitCompCalcCompDate:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
   AttributeSetShortDescription:string,
   PartAttrClassID:string,
      /**  Revision Number associated with Part  */  
   RevisionNum:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CapPromiseRow{
   Company:string,
   OrderNum:number,
   GlobalCTP:boolean,
   EnableGlobalCTP:boolean,
   ProjectedStartDate:string,
   AllowSetOrderPromiseDate:boolean,
      /**  Indicates the Shipment Option to be used during CTP processing.  Can be "SOC" - Ship Order Complete, "SLC" - Ship Line Complete or "SPQ" - Ship Partial Quantities.  */  
   ShipOption:string,
      /**  Demand Contract Number  */  
   DemandContractNum:number,
      /**  DemandHeadSeq  */  
   DemandHeadSeq:number,
      /**  Demand Contract Description  */  
   DemandContract:string,
      /**  PO Number for Demand Entry Logic  */  
   PONum:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CapPromiseTableset{
   CapPromise:Erp_Tablesets_CapPromiseRow[],
   CapPromiseDtl:Erp_Tablesets_CapPromiseDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param PartNum
      @param QtyIn
      @param fromuom
      @param touom
   */  
export interface FindMaxConv_input{
   PartNum:string,
   QtyIn:number,
   fromuom:string,
   touom:string,
}

export interface FindMaxConv_output{
parameters : {
      /**  output parameters  */  
   maxQty:number,
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

   /** Required : 
      @param ds
   */  
export interface SetOrderPromiseDate_input{
   ds:Erp_Tablesets_CapPromiseTableset[],
}

export interface SetOrderPromiseDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CapPromiseTableset[],
}
}

export interface deleteJob_output{
}

