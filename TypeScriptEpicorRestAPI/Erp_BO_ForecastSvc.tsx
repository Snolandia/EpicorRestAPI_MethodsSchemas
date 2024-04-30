import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.ForecastSvc
// Description: 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/$metadata", {
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

   /**  
   Summary: Calls GetRows for the service
   Description: Get Forecasts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Forecasts
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ForecastRow
   */  
export function get_Forecasts(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ForecastRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/Forecasts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ForecastRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Forecasts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ForecastRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ForecastRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Forecasts(requestBody:Erp_Tablesets_ForecastRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/Forecasts", {
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
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the Forecast item
   Description: Calls GetByID to retrieve the Forecast item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Forecast
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param ForeDate Desc: ForeDate   Required: True   Allow empty value : True
      @param AttributeSetID Desc: AttributeSetID   Required: True
      @param ParentPartNum Desc: ParentPartNum   Required: True   Allow empty value : True
      @param ShipToNum Desc: ShipToNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ForecastRow
   */  
export function get_Forecasts_Company_PartNum_Plant_CustNum_ForeDate_AttributeSetID_ParentPartNum_ShipToNum(Company:string, PartNum:string, Plant:string, CustNum:string, ForeDate:string, AttributeSetID:string, ParentPartNum:string, ShipToNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ForecastRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/Forecasts(" + Company + "," + PartNum + "," + Plant + "," + CustNum + "," + ForeDate + "," + AttributeSetID + "," + ParentPartNum + "," + ShipToNum + ")", {
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
         resolve(data as Erp_Tablesets_ForecastRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update Forecast for the service
   Description: Calls UpdateExt to update Forecast. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Forecast
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param ForeDate Desc: ForeDate   Required: True   Allow empty value : True
      @param AttributeSetID Desc: AttributeSetID   Required: True
      @param ParentPartNum Desc: ParentPartNum   Required: True   Allow empty value : True
      @param ShipToNum Desc: ShipToNum   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ForecastRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_Forecasts_Company_PartNum_Plant_CustNum_ForeDate_AttributeSetID_ParentPartNum_ShipToNum(Company:string, PartNum:string, Plant:string, CustNum:string, ForeDate:string, AttributeSetID:string, ParentPartNum:string, ShipToNum:string, requestBody:Erp_Tablesets_ForecastRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/Forecasts(" + Company + "," + PartNum + "," + Plant + "," + CustNum + "," + ForeDate + "," + AttributeSetID + "," + ParentPartNum + "," + ShipToNum + ")", {
          method: 'patch',
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
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete Forecast item
   Description: Call UpdateExt to delete Forecast item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Forecast
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param ForeDate Desc: ForeDate   Required: True   Allow empty value : True
      @param AttributeSetID Desc: AttributeSetID   Required: True
      @param ParentPartNum Desc: ParentPartNum   Required: True   Allow empty value : True
      @param ShipToNum Desc: ShipToNum   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_Forecasts_Company_PartNum_Plant_CustNum_ForeDate_AttributeSetID_ParentPartNum_ShipToNum(Company:string, PartNum:string, Plant:string, CustNum:string, ForeDate:string, AttributeSetID:string, ParentPartNum:string, ShipToNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/Forecasts(" + Company + "," + PartNum + "," + Plant + "," + CustNum + "," + ForeDate + "," + AttributeSetID + "," + ParentPartNum + "," + ShipToNum + ")", {
          method: 'delete',
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

   /**  
   Summary: Calls GetByID for the service
   Description: Get ForecastAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ForecastAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param ForeDate Desc: ForeDate   Required: True   Allow empty value : True
      @param AttributeSetID Desc: AttributeSetID   Required: True
      @param ParentPartNum Desc: ParentPartNum   Required: True   Allow empty value : True
      @param ShipToNum Desc: ShipToNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ForecastAttchRow
   */  
export function get_Forecasts_Company_PartNum_Plant_CustNum_ForeDate_AttributeSetID_ParentPartNum_ShipToNum_ForecastAttches(Company:string, PartNum:string, Plant:string, CustNum:string, ForeDate:string, AttributeSetID:string, ParentPartNum:string, ShipToNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ForecastAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/Forecasts(" + Company + "," + PartNum + "," + Plant + "," + CustNum + "," + ForeDate + "," + AttributeSetID + "," + ParentPartNum + "," + ShipToNum + ")/ForecastAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ForecastAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ForecastAttch item
   Description: Calls GetByID to retrieve the ForecastAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ForecastAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param ForeDate Desc: ForeDate   Required: True   Allow empty value : True
      @param AttributeSetID Desc: AttributeSetID   Required: True
      @param ParentPartNum Desc: ParentPartNum   Required: True   Allow empty value : True
      @param ShipToNum Desc: ShipToNum   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ForecastAttchRow
   */  
export function get_Forecasts_Company_PartNum_Plant_CustNum_ForeDate_AttributeSetID_ParentPartNum_ShipToNum_ForecastAttches_Company_PartNum_Plant_CustNum_ForeDate_AttributeSetID_ParentPartNum_ShipToNum_DrawingSeq(Company:string, PartNum:string, Plant:string, CustNum:string, ForeDate:string, AttributeSetID:string, ParentPartNum:string, ShipToNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ForecastAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/Forecasts(" + Company + "," + PartNum + "," + Plant + "," + CustNum + "," + ForeDate + "," + AttributeSetID + "," + ParentPartNum + "," + ShipToNum + ")/ForecastAttches(" + Company + "," + PartNum + "," + Plant + "," + CustNum + "," + ForeDate + "," + AttributeSetID + "," + ParentPartNum + "," + ShipToNum + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_ForecastAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get ForecastAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ForecastAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ForecastAttchRow
   */  
export function get_ForecastAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ForecastAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/ForecastAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ForecastAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ForecastAttches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ForecastAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ForecastAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ForecastAttches(requestBody:Erp_Tablesets_ForecastAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/ForecastAttches", {
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
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ForecastAttch item
   Description: Calls GetByID to retrieve the ForecastAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ForecastAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param ForeDate Desc: ForeDate   Required: True   Allow empty value : True
      @param AttributeSetID Desc: AttributeSetID   Required: True
      @param ParentPartNum Desc: ParentPartNum   Required: True   Allow empty value : True
      @param ShipToNum Desc: ShipToNum   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ForecastAttchRow
   */  
export function get_ForecastAttches_Company_PartNum_Plant_CustNum_ForeDate_AttributeSetID_ParentPartNum_ShipToNum_DrawingSeq(Company:string, PartNum:string, Plant:string, CustNum:string, ForeDate:string, AttributeSetID:string, ParentPartNum:string, ShipToNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ForecastAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/ForecastAttches(" + Company + "," + PartNum + "," + Plant + "," + CustNum + "," + ForeDate + "," + AttributeSetID + "," + ParentPartNum + "," + ShipToNum + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_ForecastAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ForecastAttch for the service
   Description: Calls UpdateExt to update ForecastAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ForecastAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param ForeDate Desc: ForeDate   Required: True   Allow empty value : True
      @param AttributeSetID Desc: AttributeSetID   Required: True
      @param ParentPartNum Desc: ParentPartNum   Required: True   Allow empty value : True
      @param ShipToNum Desc: ShipToNum   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ForecastAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ForecastAttches_Company_PartNum_Plant_CustNum_ForeDate_AttributeSetID_ParentPartNum_ShipToNum_DrawingSeq(Company:string, PartNum:string, Plant:string, CustNum:string, ForeDate:string, AttributeSetID:string, ParentPartNum:string, ShipToNum:string, DrawingSeq:string, requestBody:Erp_Tablesets_ForecastAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/ForecastAttches(" + Company + "," + PartNum + "," + Plant + "," + CustNum + "," + ForeDate + "," + AttributeSetID + "," + ParentPartNum + "," + ShipToNum + "," + DrawingSeq + ")", {
          method: 'patch',
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
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete ForecastAttch item
   Description: Call UpdateExt to delete ForecastAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ForecastAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param ForeDate Desc: ForeDate   Required: True   Allow empty value : True
      @param AttributeSetID Desc: AttributeSetID   Required: True
      @param ParentPartNum Desc: ParentPartNum   Required: True   Allow empty value : True
      @param ShipToNum Desc: ShipToNum   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ForecastAttches_Company_PartNum_Plant_CustNum_ForeDate_AttributeSetID_ParentPartNum_ShipToNum_DrawingSeq(Company:string, PartNum:string, Plant:string, CustNum:string, ForeDate:string, AttributeSetID:string, ParentPartNum:string, ShipToNum:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/ForecastAttches(" + Company + "," + PartNum + "," + Plant + "," + CustNum + "," + ForeDate + "," + AttributeSetID + "," + ParentPartNum + "," + ShipToNum + "," + DrawingSeq + ")", {
          method: 'delete',
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

   /**  
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ForecastListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ForecastListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ForecastListRow)
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
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseForecast:string, whereClauseForecastAttch:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseForecast!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseForecast=" + whereClauseForecast
   }
   if(typeof whereClauseForecastAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseForecastAttch=" + whereClauseForecastAttch
   }
   if(typeof pageSize!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "pageSize=" + pageSize
   }
   if(typeof absolutePage!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "absolutePage=" + absolutePage
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRows_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/GetRows" + params, {
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
         resolve(data as GetRows_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True   Allow empty value : True
   Required: True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(partNum:string, plant:string, custNum:string, foreDate:string, attributeSetID:string, parentPartNum:string, shipToNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof partNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "partNum=" + partNum
   }
   if(typeof plant!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "plant=" + plant
   }
   if(typeof custNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "custNum=" + custNum
   }
   if(typeof foreDate!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "foreDate=" + foreDate
   }
   if(typeof attributeSetID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "attributeSetID=" + attributeSetID
   }
   if(typeof parentPartNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "parentPartNum=" + parentPartNum
   }
   if(typeof shipToNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "shipToNum=" + shipToNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/GetByID" + params, {
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
         resolve(data as GetByID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      @param whereClause Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      @param pageSize Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      @param absolutePage Desc: Page of rows to return.   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetList(whereClause:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClause!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClause=" + whereClause
   }
   if(typeof pageSize!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "pageSize=" + pageSize
   }
   if(typeof absolutePage!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "absolutePage=" + absolutePage
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/GetList" + params, {
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
         resolve(data as GetList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ClearForecasts
   Description: This method deletes all Forecast records for the Current Plant, or all Plants, with two exceptions:
- Forecasts for Global Parts are not deleted
- Forecasts marked as autoTransfer are not deleted.
   OperationID: ClearForecasts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ClearForecasts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClearForecasts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ClearForecasts(requestBody:ClearForecasts_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ClearForecasts_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/ClearForecasts", {
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
         resolve(data as ClearForecasts_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ClearShipToForecasts
   Description: This method removes the ShipToNum from all the Forecasts
   OperationID: ClearShipToForecasts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClearShipToForecasts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ClearShipToForecasts(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ClearShipToForecasts_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/ClearShipToForecasts", {
          method: 'post',
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
         resolve(data as ClearShipToForecasts_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingShipTo
   Description: Validate the ShipTo Id.
   OperationID: OnChangingShipTo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingShipTo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingShipTo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingShipTo(requestBody:OnChangingShipTo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingShipTo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/OnChangingShipTo", {
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
         resolve(data as OnChangingShipTo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ExportForecasts
   Description: This method exports all Forecast records for the current company, after the given date.
            
If ForecastImportExport records are present as input, they are used to build the following
lists for selection of records:
PlantList
PartList
CustNumList
If a record in the input dataset:
1) has a value for Plant, PartNum, or CustID and blank values for the other two, and
2) blank values for the fields ImportErrorMsg and ForeQty,
then the value in Plant, PartNum, or CustID will be added to the respective
list.
If a record has a value in more than one of these fields, it will be ignored.
            
After the above lists have been constructed, the record selection will use the lists as follows:
- if a list is non-empty, only records whose corresponding field value appears in the list
will be a candidate for being included in the returned dataset, subject to the other conditions
- if a list is empty, no filtering will occur on the values for that field, except possibly
conditions in the "whereClauseForecast" parameter.
   OperationID: ExportForecasts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ExportForecasts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportForecasts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExportForecasts(requestBody:ExportForecasts_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ExportForecasts_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/ExportForecasts", {
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
         resolve(data as ExportForecasts_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ConvertForecastsToCSV
   Description: This method receives a ForecastImportExportTableset and returns a CSV file to export
   OperationID: ConvertForecastsToCSV
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ConvertForecastsToCSV_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ConvertForecastsToCSV_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ConvertForecastsToCSV(requestBody:ConvertForecastsToCSV_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ConvertForecastsToCSV_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/ConvertForecastsToCSV", {
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
         resolve(data as ConvertForecastsToCSV_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ImportForecastsReadFile
   Description: This methods receives a CSV file Path and imports the Forecasts found
   OperationID: ImportForecastsReadFile
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ImportForecastsReadFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportForecastsReadFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportForecastsReadFile(requestBody:ImportForecastsReadFile_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ImportForecastsReadFile_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/ImportForecastsReadFile", {
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
         resolve(data as ImportForecastsReadFile_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNextDateNewForecast
   Description: Calculates the next ForeDate from the Forecast selected before the GetNew operation
   OperationID: GetNextDateNewForecast
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNextDateNewForecast_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNextDateNewForecast_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNextDateNewForecast(requestBody:GetNextDateNewForecast_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNextDateNewForecast_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/GetNextDateNewForecast", {
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
         resolve(data as GetNextDateNewForecast_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetForecastDays
   Description: To retrieve the ForecastDaysBefore and ForecastDaysAfter from the JC system settings.
   OperationID: GetForecastDays
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetForecastDays_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetForecastDays_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetForecastDays(requestBody:GetForecastDays_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetForecastDays_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/GetForecastDays", {
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
         resolve(data as GetForecastDays_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewForecastImportExport
   Description: This method creates a new ForecastImportExport dataset row.
   OperationID: GetNewForecastImportExport
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewForecastImportExport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewForecastImportExport_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewForecastImportExport(requestBody:GetNewForecastImportExport_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewForecastImportExport_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/GetNewForecastImportExport", {
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
         resolve(data as GetNewForecastImportExport_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSalesHistory
   Description: This method provides a ForecastSalesHistory dataset filled with Sales History data.  This can
be used as the basis of the External Forecast Export.
            
Notes:      taken from mre10-sm-ex-dg.w (PROCEDURE Export-Forecast)
   OperationID: GetSalesHistory
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetSalesHistory_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSalesHistory_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSalesHistory(requestBody:GetSalesHistory_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetSalesHistory_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/GetSalesHistory", {
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
         resolve(data as GetSalesHistory_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ImportExternalForecast
   Description: This method populates the ttForecastImportExport dataset with forecast data.
   OperationID: ImportExternalForecast
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ImportExternalForecast_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportExternalForecast_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportExternalForecast(requestBody:ImportExternalForecast_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ImportExternalForecast_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/ImportExternalForecast", {
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
         resolve(data as ImportExternalForecast_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ImportForecasts
   Description: This method conditionally adds/overwrites Forecast records using the same logic as
the Vantage Forecast Import screen.
   OperationID: ImportForecasts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ImportForecasts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportForecasts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportForecasts(requestBody:ImportForecasts_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ImportForecasts_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/ImportForecasts", {
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
         resolve(data as ImportForecasts_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method IsConfigurable
   OperationID: IsConfigurable
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/IsConfigurable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsConfigurable_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IsConfigurable(requestBody:IsConfigurable_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<IsConfigurable_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/IsConfigurable", {
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
         resolve(data as IsConfigurable_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateAttributeSetIDFromRevisionNum
   Description: This method updates attributeSetID and planningAttributeSetSeq when new revision is selected.
   OperationID: UpdateAttributeSetIDFromRevisionNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateAttributeSetIDFromRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateAttributeSetIDFromRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateAttributeSetIDFromRevisionNum(requestBody:UpdateAttributeSetIDFromRevisionNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateAttributeSetIDFromRevisionNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/UpdateAttributeSetIDFromRevisionNum", {
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
         resolve(data as UpdateAttributeSetIDFromRevisionNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PartsAttributeClassHasRevisionAndIsMRPTracked
   Description: This method updates attributeSetID and planningAttributeSetSeq when new revision is selected.
   OperationID: PartsAttributeClassHasRevisionAndIsMRPTracked
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PartsAttributeClassHasRevisionAndIsMRPTracked_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PartsAttributeClassHasRevisionAndIsMRPTracked_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PartsAttributeClassHasRevisionAndIsMRPTracked(requestBody:PartsAttributeClassHasRevisionAndIsMRPTracked_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PartsAttributeClassHasRevisionAndIsMRPTracked_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/PartsAttributeClassHasRevisionAndIsMRPTracked", {
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
         resolve(data as PartsAttributeClassHasRevisionAndIsMRPTracked_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewForecast
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewForecast
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewForecast_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewForecast_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewForecast(requestBody:GetNewForecast_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewForecast_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/GetNewForecast", {
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
         resolve(data as GetNewForecast_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewForecastAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewForecastAttch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewForecastAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewForecastAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewForecastAttch(requestBody:GetNewForecastAttch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewForecastAttch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/GetNewForecastAttch", {
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
         resolve(data as GetNewForecastAttch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteByID(requestBody:DeleteByID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/DeleteByID", {
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
         resolve(data as DeleteByID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetBySysRowID(id:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof id!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "id=" + id
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetBySysRowID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/GetBySysRowID" + params, {
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
         resolve(data as GetBySysRowID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetBySysRowIDs(ids:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof ids!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "ids=" + ids
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetBySysRowIDs_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/GetBySysRowIDs" + params, {
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
         resolve(data as GetBySysRowIDs_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
   OperationID: Update
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Update(requestBody:Update_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Update_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/Update", {
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
         resolve(data as Update_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateExt(requestBody:UpdateExt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateExt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/UpdateExt", {
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
         resolve(data as UpdateExt_output)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ForecastAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ForecastAttchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ForecastListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ForecastListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ForecastRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ForecastRow,
}

export interface Erp_Tablesets_ForecastAttchRow{
   "Company":string,
   "PartNum":string,
   "Plant":string,
   "CustNum":number,
   "ForeDate":string,
   "AttributeSetID":number,
   "ParentPartNum":string,
   "ShipToNum":string,
   "DrawingSeq":number,
   "XFileRefNum":number,
   "SysRevID":number,
   "SysRowID":string,
   "ForeignSysRowID":string,
   "DrawDesc":string,
   "FileName":string,
   "PDMDocID":string,
   "DocTypeID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ForecastListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A  unique integer assigned by the system to new customers by the customer maintenance program. This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never need to know about the value of this field.  */  
   "CustNum":number,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   "PartNum":string,
      /**  Site id for this forecast  */  
   "Plant":string,
      /**  Date at which this forecast is considered effective.  This date is used to control the building of inventory based on this forecast.  */  
   "ForeDate":string,
      /**  Inactive flag  */  
   "Inactive":boolean,
      /**  Forecast quantity  */  
   "ForeQty":number,
   "ForeQtyUOM":string,
      /**  The current accumulated quantity from all the order releases that fall within the forecast horizon.  */  
   "ConsumedQty":number,
      /**  Inbound Customer PO Number  */  
   "PONum":string,
      /**  The user ID that created this batch.  */  
   "CreatedBy":string,
      /**  Date the forecast was created  */  
   "CreatedDate":string,
      /**  Auto Transfer flag  */  
   "AutoTransfer":boolean,
      /**  The reference from the incoming demand source.  Can be used to locate other forecast records that have been created by this demand.  */  
   "DemandReference":string,
      /**  The DemandContractHdr to which this Forecast is related.  */  
   "DemandContractNum":number,
      /**  The sequence from the DemandHead record this Forecast is related to.  */  
   "DemandHeadSeq":number,
      /**  An internal identifier to group demand schedules together.  Will link the Forecast record to the DemandSchedule that created it.  */  
   "ScheduleNumber":string,
      /**  Shipto.ShipToNum.  For future use.  */  
   "ShipToNum":string,
      /**  Date until this forecast is considered effective. for information purposes only. for future use.  */  
   "EndDate":string,
      /**  The ParentPartNum field identifies the Parent Part for kit components.  */  
   "ParentPartNum":string,
      /**   A character flag field used to differentiate between kit component types
P = Kit Parent line
C = Kit Component Line
Null = regular line  */  
   "KitFlag":string,
      /**  Last update done by EDI to the forecast  */  
   "EDIUpdateDate":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Reason import of this record failed.  Blank implies no error occurred.  */  
   "ImportErrorMsg":string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   "CustomerBTName":string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   "CustomerCustID":string,
      /**  The full name of the customer.  */  
   "CustomerName":string,
      /**  The unique identifier of the demand contract.  This must be unique for a customer.  */  
   "DemandContractDemandContract":string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   "PartNumSellingFactor":number,
      /**  Indicates if this part is serial number tracked  */  
   "PartNumTrackSerialNum":boolean,
      /**  Describes the Part.  */  
   "PartNumPartDescription":string,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   "PartNumPricePerCode":string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   "PartNumTrackDimension":boolean,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   "PartNumIUM":string,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   "PartNumSalesUM":string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   "PartNumTrackLots":boolean,
      /**  The Plant name. Used on shipping reports.  */  
   "PlantName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ForecastRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A  unique integer assigned by the system to new customers by the customer maintenance program. This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never need to know about the value of this field.  */  
   "CustNum":number,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   "PartNum":string,
      /**  Site id for this forecast  */  
   "Plant":string,
      /**  Date at which this forecast is considered effective.  This date is used to control the building of inventory based on this forecast.  */  
   "ForeDate":string,
      /**  Inactive flag  */  
   "Inactive":boolean,
      /**  Forecast quantity  */  
   "ForeQty":number,
   "ForeQtyUOM":string,
      /**  The current accumulated quantity from all the order releases that fall within the forecast horizon.  */  
   "ConsumedQty":number,
      /**  Inbound Customer PO Number  */  
   "PONum":string,
      /**  The user ID that created this batch.  */  
   "CreatedBy":string,
      /**  Date the forecast was created  */  
   "CreatedDate":string,
      /**  Auto Transfer flag  */  
   "AutoTransfer":boolean,
      /**  The reference from the incoming demand source.  Can be used to locate other forecast records that have been created by this demand.  */  
   "DemandReference":string,
      /**  The DemandContractHdr to which this Forecast is related.  */  
   "DemandContractNum":number,
      /**  The sequence from the DemandHead record this Forecast is related to.  */  
   "DemandHeadSeq":number,
      /**  An internal identifier to group demand schedules together.  Will link the Forecast record to the DemandSchedule that created it.  */  
   "ScheduleNumber":string,
      /**  Shipto.ShipToNum.  For future use.  */  
   "ShipToNum":string,
      /**  Date until this forecast is considered effective. for information purposes only. for future use.  */  
   "EndDate":string,
      /**  The ParentPartNum field identifies the Parent Part for kit components.  */  
   "ParentPartNum":string,
      /**   A character flag field used to differentiate between kit component types
P = Kit Parent line
C = Kit Component Line
Null = regular line  */  
   "KitFlag":string,
      /**  Last update done by EDI to the forecast  */  
   "EDIUpdateDate":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "RevisionNum":string,
      /**  Reason import of this record failed.  Blank implies no error occurred.  */  
   "ImportErrorMsg":string,
   "AttributeSetShortDescription":string,
   "AttributeSetDescription":string,
   "PlanningAttributeSetSeq":number,
   "BitFlag":number,
   "CustomerBTName":string,
   "CustomerName":string,
   "CustomerCustID":string,
   "DemandContractDemandContract":string,
   "PartNumAttrClassID":string,
   "PartNumSellingFactor":number,
   "PartNumTrackSerialNum":boolean,
   "PartNumTrackDimension":boolean,
   "PartNumSalesUM":string,
   "PartNumPartDescription":string,
   "PartNumTrackLots":boolean,
   "PartNumPricePerCode":string,
   "PartNumIUM":string,
   "PlantName":string,
      /**  RowMod  */  
   "RowMod":string,
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
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param plAllPlants
      @param pdFromDate
   */  
export interface ClearForecasts_input{
      /**  If TRUE, clear all plants; if FALSE, clear Current Plant.  */  
   plAllPlants:boolean,
      /**  Only Forecast records on or after the given date will be deleted.  */  
   pdFromDate:string,
}

export interface ClearForecasts_output{
}

export interface ClearShipToForecasts_output{
}

   /** Required : 
      @param ds
      @param exportFilename
   */  
export interface ConvertForecastsToCSV_input{
   ds:Erp_Tablesets_ForecastImportExportTableset[],
      /**  Name of the new file to be converted  */  
   exportFilename:string,
}

export interface ConvertForecastsToCSV_output{
      /**  File Path on server  */  
   returnObj:string,
parameters : {
      /**  output parameters  */  
   count:number,
}
}

   /** Required : 
      @param partNum
      @param plant
      @param custNum
      @param foreDate
      @param attributeSetID
      @param parentPartNum
      @param shipToNum
   */  
export interface DeleteByID_input{
   partNum:string,
   plant:string,
   custNum:number,
   foreDate:string,
   attributeSetID:number,
   parentPartNum:string,
   shipToNum:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_ForecastAttchRow{
   Company:string,
   PartNum:string,
   Plant:string,
   CustNum:number,
   ForeDate:string,
   AttributeSetID:number,
   ParentPartNum:string,
   ShipToNum:string,
   DrawingSeq:number,
   XFileRefNum:number,
   SysRevID:number,
   SysRowID:string,
   ForeignSysRowID:string,
   DrawDesc:string,
   FileName:string,
   PDMDocID:string,
   DocTypeID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ForecastImportExportRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier of this plant assigned by the user.  */  
   Plant:string,
      /**  A unique part number that identifies this part.  */  
   PartNum:string,
      /**  A user defined external customer ID.  A blank CustID is used for a non-Customer-specific forecast.  */  
   CustID:string,
      /**  Date at which this forecast is considered effective.  This date is used to control the building of inventory based on this forecast.  */  
   ForeDate:string,
   ForeQty:number,
      /**  The current accumulated quantity from all the order releases that fall within the forecast horizon.  */  
   ConsumedQty:number,
      /**  Reason import of this record failed.  Blank implies no error occurred.  */  
   ImportErrorMsg:string,
      /**  External forecast period  */  
   ExtFcstPeriod:string,
   ShipToNum:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ForecastImportExportTableset{
   ForecastImportExport:Erp_Tablesets_ForecastImportExportRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ForecastListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A  unique integer assigned by the system to new customers by the customer maintenance program. This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never need to know about the value of this field.  */  
   CustNum:number,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   PartNum:string,
      /**  Site id for this forecast  */  
   Plant:string,
      /**  Date at which this forecast is considered effective.  This date is used to control the building of inventory based on this forecast.  */  
   ForeDate:string,
      /**  Inactive flag  */  
   Inactive:boolean,
      /**  Forecast quantity  */  
   ForeQty:number,
   ForeQtyUOM:string,
      /**  The current accumulated quantity from all the order releases that fall within the forecast horizon.  */  
   ConsumedQty:number,
      /**  Inbound Customer PO Number  */  
   PONum:string,
      /**  The user ID that created this batch.  */  
   CreatedBy:string,
      /**  Date the forecast was created  */  
   CreatedDate:string,
      /**  Auto Transfer flag  */  
   AutoTransfer:boolean,
      /**  The reference from the incoming demand source.  Can be used to locate other forecast records that have been created by this demand.  */  
   DemandReference:string,
      /**  The DemandContractHdr to which this Forecast is related.  */  
   DemandContractNum:number,
      /**  The sequence from the DemandHead record this Forecast is related to.  */  
   DemandHeadSeq:number,
      /**  An internal identifier to group demand schedules together.  Will link the Forecast record to the DemandSchedule that created it.  */  
   ScheduleNumber:string,
      /**  Shipto.ShipToNum.  For future use.  */  
   ShipToNum:string,
      /**  Date until this forecast is considered effective. for information purposes only. for future use.  */  
   EndDate:string,
      /**  The ParentPartNum field identifies the Parent Part for kit components.  */  
   ParentPartNum:string,
      /**   A character flag field used to differentiate between kit component types
P = Kit Parent line
C = Kit Component Line
Null = regular line  */  
   KitFlag:string,
      /**  Last update done by EDI to the forecast  */  
   EDIUpdateDate:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Reason import of this record failed.  Blank implies no error occurred.  */  
   ImportErrorMsg:string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   CustomerBTName:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   CustomerCustID:string,
      /**  The full name of the customer.  */  
   CustomerName:string,
      /**  The unique identifier of the demand contract.  This must be unique for a customer.  */  
   DemandContractDemandContract:string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   PartNumSellingFactor:number,
      /**  Indicates if this part is serial number tracked  */  
   PartNumTrackSerialNum:boolean,
      /**  Describes the Part.  */  
   PartNumPartDescription:string,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   PartNumPricePerCode:string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   PartNumTrackDimension:boolean,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   PartNumIUM:string,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   PartNumSalesUM:string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   PartNumTrackLots:boolean,
      /**  The Plant name. Used on shipping reports.  */  
   PlantName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ForecastListTableset{
   ForecastList:Erp_Tablesets_ForecastListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ForecastRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A  unique integer assigned by the system to new customers by the customer maintenance program. This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never need to know about the value of this field.  */  
   CustNum:number,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   PartNum:string,
      /**  Site id for this forecast  */  
   Plant:string,
      /**  Date at which this forecast is considered effective.  This date is used to control the building of inventory based on this forecast.  */  
   ForeDate:string,
      /**  Inactive flag  */  
   Inactive:boolean,
      /**  Forecast quantity  */  
   ForeQty:number,
   ForeQtyUOM:string,
      /**  The current accumulated quantity from all the order releases that fall within the forecast horizon.  */  
   ConsumedQty:number,
      /**  Inbound Customer PO Number  */  
   PONum:string,
      /**  The user ID that created this batch.  */  
   CreatedBy:string,
      /**  Date the forecast was created  */  
   CreatedDate:string,
      /**  Auto Transfer flag  */  
   AutoTransfer:boolean,
      /**  The reference from the incoming demand source.  Can be used to locate other forecast records that have been created by this demand.  */  
   DemandReference:string,
      /**  The DemandContractHdr to which this Forecast is related.  */  
   DemandContractNum:number,
      /**  The sequence from the DemandHead record this Forecast is related to.  */  
   DemandHeadSeq:number,
      /**  An internal identifier to group demand schedules together.  Will link the Forecast record to the DemandSchedule that created it.  */  
   ScheduleNumber:string,
      /**  Shipto.ShipToNum.  For future use.  */  
   ShipToNum:string,
      /**  Date until this forecast is considered effective. for information purposes only. for future use.  */  
   EndDate:string,
      /**  The ParentPartNum field identifies the Parent Part for kit components.  */  
   ParentPartNum:string,
      /**   A character flag field used to differentiate between kit component types
P = Kit Parent line
C = Kit Component Line
Null = regular line  */  
   KitFlag:string,
      /**  Last update done by EDI to the forecast  */  
   EDIUpdateDate:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
      /**  Reason import of this record failed.  Blank implies no error occurred.  */  
   ImportErrorMsg:string,
   AttributeSetShortDescription:string,
   AttributeSetDescription:string,
   PlanningAttributeSetSeq:number,
   BitFlag:number,
   CustomerBTName:string,
   CustomerName:string,
   CustomerCustID:string,
   DemandContractDemandContract:string,
   PartNumAttrClassID:string,
   PartNumSellingFactor:number,
   PartNumTrackSerialNum:boolean,
   PartNumTrackDimension:boolean,
   PartNumSalesUM:string,
   PartNumPartDescription:string,
   PartNumTrackLots:boolean,
   PartNumPricePerCode:string,
   PartNumIUM:string,
   PlantName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ForecastSalesHistoryRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   PartNum:string,
      /**  Invoice date is duplicated from the InvcGrp record.  */  
   InvoiceDate:string,
      /**  Selling Quantity Shipped/billed (or MISSING)  */  
   SellingShipQty:string,
      /**  Customer associated with invoice  */  
   CustID:string,
      /**  Plant associated with invoice.  */  
   Plant:string,
      /**  Year of the first period for this sales history export.  */  
   StartYear:number,
      /**  Period of the year corresponding to the first available sales history.  */  
   StartPeriod:number,
      /**  Periods per year  */  
   PeriodsPerYear:number,
      /**  Periods per cycle.  */  
   PeriodsPerCycle:number,
      /**  Date of this period  */  
   PeriodDate:string,
      /**  Name of this period  */  
   PeriodName:string,
      /**  Part Description  */  
   PartDescription:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ForecastSalesHistoryTableset{
   ForecastSalesHistory:Erp_Tablesets_ForecastSalesHistoryRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ForecastTableset{
   Forecast:Erp_Tablesets_ForecastRow[],
   ForecastAttch:Erp_Tablesets_ForecastAttchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtForecastTableset{
   Forecast:Erp_Tablesets_ForecastRow[],
   ForecastAttch:Erp_Tablesets_ForecastAttchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ds
      @param whereClauseForecast
      @param pdFromDate
      @param pageSize
      @param absolutePage
   */  
export interface ExportForecasts_input{
   ds:Erp_Tablesets_ForecastImportExportTableset[],
      /**  (optional)Additional Where conditions for Forecast table.  */  
   whereClauseForecast:string,
      /**  (optional)Only records on or after the given date will be considered for import.  */  
   pdFromDate:string,
      /**  For future use.  */  
   pageSize:number,
      /**  For future use.  */  
   absolutePage:number,
}

export interface ExportForecasts_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ForecastImportExportTableset,
   morePages:boolean,
}
}

   /** Required : 
      @param partNum
      @param plant
      @param custNum
      @param foreDate
      @param attributeSetID
      @param parentPartNum
      @param shipToNum
   */  
export interface GetByID_input{
   partNum:string,
   plant:string,
   custNum:number,
   foreDate:string,
   attributeSetID:number,
   parentPartNum:string,
   shipToNum:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_ForecastTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_ForecastTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_ForecastTableset[],
}

   /** Required : 
      @param ipPartNum
      @param ipAttributeSetID
      @param ipPlant
   */  
export interface GetForecastDays_input{
      /**  Part Number  */  
   ipPartNum:string,
      /**  Attribute Set ID  */  
   ipAttributeSetID:number,
      /**  Site  */  
   ipPlant:string,
}

export interface GetForecastDays_output{
parameters : {
      /**  output parameters  */  
   piDaysBefore:number,
   piDaysAfter:number,
}
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetList_input{
      /**  An expression used to filter the rows. Can be left blank for all rows.  */  
   whereClause:string,
      /**  The maximum number of rows to return. Leave as zero for no maximum.  */  
   pageSize:number,
      /**  Page of rows to return.  */  
   absolutePage:number,
}

export interface GetList_output{
   returnObj:Erp_Tablesets_ForecastListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param partNum
      @param plant
      @param custNum
      @param foreDate
      @param attributeSetID
      @param parentPartNum
      @param shipToNum
   */  
export interface GetNewForecastAttch_input{
   ds:Erp_Tablesets_ForecastTableset[],
   partNum:string,
   plant:string,
   custNum:number,
   foreDate:string,
   attributeSetID:number,
   parentPartNum:string,
   shipToNum:string,
}

export interface GetNewForecastAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ForecastTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewForecastImportExport_input{
   ds:Erp_Tablesets_ForecastImportExportTableset[],
}

export interface GetNewForecastImportExport_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ForecastImportExportTableset,
}
}

   /** Required : 
      @param ds
      @param partNum
      @param plant
      @param custNum
      @param foreDate
      @param attributeSetID
      @param parentPartNum
   */  
export interface GetNewForecast_input{
   ds:Erp_Tablesets_ForecastTableset[],
   partNum:string,
   plant:string,
   custNum:number,
   foreDate:string,
   attributeSetID:number,
   parentPartNum:string,
}

export interface GetNewForecast_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ForecastTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNextDateNewForecast_input{
   ds:Erp_Tablesets_ForecastTableset[],
}

export interface GetNextDateNewForecast_output{
      /**  DateTime used for the next Forecast to be added  */  
   returnObj:string,
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ForecastTableset,
}
}

   /** Required : 
      @param whereClauseForecast
      @param whereClauseForecastAttch
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseForecast:string,
   whereClauseForecastAttch:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_ForecastTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param pdBeginDate
      @param pdEndDate
      @param pcCustList
      @param pcCustGrpList
      @param pcPartList
      @param pcProdGrpList
      @param pcPlantList
      @param pcOutputFile
      @param pcOutputFormat
   */  
export interface GetSalesHistory_input{
      /**  Begin Date of Sales to extract.  */  
   pdBeginDate:string,
      /**  End Date of Sales to extract.  */  
   pdEndDate:string,
      /**  Tilde-delimited list of Customer Numbers for Sales extract.  Blank means all.  */  
   pcCustList:string,
      /**  Tilde-delimited list of Customer Group Codes for Sales extract.  Blank means all.  */  
   pcCustGrpList:string,
      /**  Tilde-delimited list of Part Numbers for Sales extract.  Blank means all.  */  
   pcPartList:string,
      /**  Tilde-delimited list of Product Group Codes for Sales extract.  Blank means all.  */  
   pcProdGrpList:string,
      /**  Tilde-delimited list of Plants for Sales extract.  Blank means all.  */  
   pcPlantList:string,
      /**  Export file path.  */  
   pcOutputFile:string,
      /**  Export output format.  */  
   pcOutputFormat:string,
}

export interface GetSalesHistory_output{
   returnObj:Erp_Tablesets_ForecastSalesHistoryTableset[],
}

export interface Ice_BOUpdErrorRow{
   TableName:string,
   ErrorLevel:string,
   ErrorType:string,
   ErrorText:string,
   ErrorSysRowID:string,
   SysRowID:string,
   RowMod:string,
}

export interface Ice_BOUpdErrorTableset{
   BOUpdError:Ice_BOUpdErrorRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
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
      @param pcImportFormat
      @param pcImportFile
   */  
export interface ImportExternalForecast_input{
      /**  Import file format.  */  
   pcImportFormat:string,
      /**  Import file path.  */  
   pcImportFile:string,
}

export interface ImportExternalForecast_output{
   returnObj:Erp_Tablesets_ForecastImportExportTableset[],
}

   /** Required : 
      @param ds
      @param fileName
      @param importFormat
   */  
export interface ImportForecastsReadFile_input{
   ds:Erp_Tablesets_ForecastImportExportTableset[],
      /**  Path to the file to import  */  
   fileName:string,
      /**  Import format  */  
   importFormat:string,
}

export interface ImportForecastsReadFile_output{
      /**  Number of rows imported  */  
   returnObj:number,
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ForecastImportExportTableset,
}
}

   /** Required : 
      @param ds
      @param pcImportOptions
      @param plAllPlants
      @param pdFromDate
   */  
export interface ImportForecasts_input{
   ds:Erp_Tablesets_ForecastImportExportTableset[],
      /**  Valid choices are "A"=Add+Replace, "C"=Clear+Reload, "N"=New.  */  
   pcImportOptions:string,
      /**  If TRUE, clear all plants; if FALSE, clear Current Plant.  */  
   plAllPlants:boolean,
      /**  Only records on or after the given date will be considered for import.  */  
   pdFromDate:string,
}

export interface ImportForecasts_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ForecastImportExportTableset,
}
}

   /** Required : 
      @param pcPartNum
   */  
export interface IsConfigurable_input{
   pcPartNum:string,
}

export interface IsConfigurable_output{
   returnObj:boolean,
}

   /** Required : 
      @param shipTo
      @param custNum
   */  
export interface OnChangingShipTo_input{
   shipTo:string,
   custNum:number,
}

export interface OnChangingShipTo_output{
}

   /** Required : 
      @param attrClassID
   */  
export interface PartsAttributeClassHasRevisionAndIsMRPTracked_input{
      /**  current Attribute Class ID  */  
   attrClassID:string,
}

export interface PartsAttributeClassHasRevisionAndIsMRPTracked_output{
   returnObj:boolean,
}

   /** Required : 
      @param partNum
      @param revisionNum
   */  
export interface UpdateAttributeSetIDFromRevisionNum_input{
      /**  current part number  */  
   partNum:string,
      /**  new revision selected  */  
   revisionNum:string,
}

export interface UpdateAttributeSetIDFromRevisionNum_output{
parameters : {
      /**  output parameters  */  
   attributeSetID:number,
   planningAttributeSetSeq:number,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtForecastTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtForecastTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_ForecastTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ForecastTableset,
}
}

