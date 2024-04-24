import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.COASegValuesSvc
// Description: Add your summary for this object here
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/$metadata", {
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

   /**  
   Summary: Calls GetRows for the service
   Description: Get COASegValues items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_COASegValues
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.COASegValuesRow
   */  
export function get_COASegValues(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COASegValuesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/COASegValues", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COASegValuesRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_COASegValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.COASegValuesRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.COASegValuesRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_COASegValues(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/COASegValues", {
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
   Summary: Calls GetByID to retrieve the COASegValue item
   Description: Calls GetByID to retrieve the COASegValue item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_COASegValue
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param SegmentNbr Desc: SegmentNbr   Required: True
      @param SegmentCode Desc: SegmentCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.COASegValuesRow
   */  
export function get_COASegValues_Company_COACode_SegmentNbr_SegmentCode(Company:string, COACode:string, SegmentNbr:string, SegmentCode:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_COASegValuesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/COASegValues(" + Company + "," + COACode + "," + SegmentNbr + "," + SegmentCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_COASegValuesRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update COASegValue for the service
   Description: Calls UpdateExt to update COASegValue. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_COASegValue
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param SegmentNbr Desc: SegmentNbr   Required: True
      @param SegmentCode Desc: SegmentCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.COASegValuesRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_COASegValues_Company_COACode_SegmentNbr_SegmentCode(Company:string, COACode:string, SegmentNbr:string, SegmentCode:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/COASegValues(" + Company + "," + COACode + "," + SegmentNbr + "," + SegmentCode + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete COASegValue item
   Description: Call UpdateExt to delete COASegValue item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_COASegValue
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param SegmentNbr Desc: SegmentNbr   Required: True
      @param SegmentCode Desc: SegmentCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_COASegValues_Company_COACode_SegmentNbr_SegmentCode(Company:string, COACode:string, SegmentNbr:string, SegmentCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/COASegValues(" + Company + "," + COACode + "," + SegmentNbr + "," + SegmentCode + ")", {
          method: 'delete',
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
   Summary: Calls GetByID for the service
   Description: Get COASegAccts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_COASegAccts1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param SegmentNbr Desc: SegmentNbr   Required: True
      @param SegmentCode Desc: SegmentCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.COASegAcctRow
   */  
export function get_COASegValues_Company_COACode_SegmentNbr_SegmentCode_COASegAccts(Company:string, COACode:string, SegmentNbr:string, SegmentCode:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COASegAcctRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/COASegValues(" + Company + "," + COACode + "," + SegmentNbr + "," + SegmentCode + ")/COASegAccts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COASegAcctRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the COASegAcct item
   Description: Calls GetByID to retrieve the COASegAcct item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_COASegAcct1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param SegmentNbr Desc: SegmentNbr   Required: True
      @param SegmentCode Desc: SegmentCode   Required: True   Allow empty value : True
      @param CurrencyCode Desc: CurrencyCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.COASegAcctRow
   */  
export function get_COASegValues_Company_COACode_SegmentNbr_SegmentCode_COASegAccts_Company_COACode_SegmentNbr_SegmentCode_CurrencyCode(Company:string, COACode:string, SegmentNbr:string, SegmentCode:string, CurrencyCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_COASegAcctRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/COASegValues(" + Company + "," + COACode + "," + SegmentNbr + "," + SegmentCode + ")/COASegAccts(" + Company + "," + COACode + "," + SegmentNbr + "," + SegmentCode + "," + CurrencyCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_COASegAcctRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get COASegOpts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_COASegOpts1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param SegmentNbr Desc: SegmentNbr   Required: True
      @param SegmentCode Desc: SegmentCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.COASegOptRow
   */  
export function get_COASegValues_Company_COACode_SegmentNbr_SegmentCode_COASegOpts(Company:string, COACode:string, SegmentNbr:string, SegmentCode:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COASegOptRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/COASegValues(" + Company + "," + COACode + "," + SegmentNbr + "," + SegmentCode + ")/COASegOpts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COASegOptRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the COASegOpt item
   Description: Calls GetByID to retrieve the COASegOpt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_COASegOpt1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param SegmentNbr Desc: SegmentNbr   Required: True
      @param SegmentCode Desc: SegmentCode   Required: True   Allow empty value : True
      @param SubSegmentNbr Desc: SubSegmentNbr   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.COASegOptRow
   */  
export function get_COASegValues_Company_COACode_SegmentNbr_SegmentCode_COASegOpts_Company_COACode_SegmentNbr_SegmentCode_SubSegmentNbr(Company:string, COACode:string, SegmentNbr:string, SegmentCode:string, SubSegmentNbr:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_COASegOptRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/COASegValues(" + Company + "," + COACode + "," + SegmentNbr + "," + SegmentCode + ")/COASegOpts(" + Company + "," + COACode + "," + SegmentNbr + "," + SegmentCode + "," + SubSegmentNbr + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_COASegOptRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get COASegRes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_COASegRes1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param SegmentNbr Desc: SegmentNbr   Required: True
      @param SegmentCode Desc: SegmentCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.COASegResRow
   */  
export function get_COASegValues_Company_COACode_SegmentNbr_SegmentCode_COASegRes(Company:string, COACode:string, SegmentNbr:string, SegmentCode:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COASegResRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/COASegValues(" + Company + "," + COACode + "," + SegmentNbr + "," + SegmentCode + ")/COASegRes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COASegResRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the COASegRe item
   Description: Calls GetByID to retrieve the COASegRe item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_COASegRe1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param SegmentNbr Desc: SegmentNbr   Required: True
      @param SegmentCode Desc: SegmentCode   Required: True   Allow empty value : True
      @param RestrictID Desc: RestrictID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.COASegResRow
   */  
export function get_COASegValues_Company_COACode_SegmentNbr_SegmentCode_COASegRes_Company_COACode_SegmentNbr_SegmentCode_RestrictID(Company:string, COACode:string, SegmentNbr:string, SegmentCode:string, RestrictID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_COASegResRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/COASegValues(" + Company + "," + COACode + "," + SegmentNbr + "," + SegmentCode + ")/COASegRes(" + Company + "," + COACode + "," + SegmentNbr + "," + SegmentCode + "," + RestrictID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_COASegResRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get COASegAccts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_COASegAccts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.COASegAcctRow
   */  
export function get_COASegAccts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COASegAcctRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/COASegAccts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COASegAcctRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_COASegAccts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.COASegAcctRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.COASegAcctRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_COASegAccts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/COASegAccts", {
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
   Summary: Calls GetByID to retrieve the COASegAcct item
   Description: Calls GetByID to retrieve the COASegAcct item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_COASegAcct
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param SegmentNbr Desc: SegmentNbr   Required: True
      @param SegmentCode Desc: SegmentCode   Required: True   Allow empty value : True
      @param CurrencyCode Desc: CurrencyCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.COASegAcctRow
   */  
export function get_COASegAccts_Company_COACode_SegmentNbr_SegmentCode_CurrencyCode(Company:string, COACode:string, SegmentNbr:string, SegmentCode:string, CurrencyCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_COASegAcctRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/COASegAccts(" + Company + "," + COACode + "," + SegmentNbr + "," + SegmentCode + "," + CurrencyCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_COASegAcctRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update COASegAcct for the service
   Description: Calls UpdateExt to update COASegAcct. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_COASegAcct
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param SegmentNbr Desc: SegmentNbr   Required: True
      @param SegmentCode Desc: SegmentCode   Required: True   Allow empty value : True
      @param CurrencyCode Desc: CurrencyCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.COASegAcctRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_COASegAccts_Company_COACode_SegmentNbr_SegmentCode_CurrencyCode(Company:string, COACode:string, SegmentNbr:string, SegmentCode:string, CurrencyCode:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/COASegAccts(" + Company + "," + COACode + "," + SegmentNbr + "," + SegmentCode + "," + CurrencyCode + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete COASegAcct item
   Description: Call UpdateExt to delete COASegAcct item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_COASegAcct
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param SegmentNbr Desc: SegmentNbr   Required: True
      @param SegmentCode Desc: SegmentCode   Required: True   Allow empty value : True
      @param CurrencyCode Desc: CurrencyCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_COASegAccts_Company_COACode_SegmentNbr_SegmentCode_CurrencyCode(Company:string, COACode:string, SegmentNbr:string, SegmentCode:string, CurrencyCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/COASegAccts(" + Company + "," + COACode + "," + SegmentNbr + "," + SegmentCode + "," + CurrencyCode + ")", {
          method: 'delete',
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
   Summary: Calls GetRows for the service
   Description: Get COASegOpts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_COASegOpts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.COASegOptRow
   */  
export function get_COASegOpts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COASegOptRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/COASegOpts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COASegOptRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_COASegOpts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.COASegOptRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.COASegOptRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_COASegOpts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/COASegOpts", {
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
   Summary: Calls GetByID to retrieve the COASegOpt item
   Description: Calls GetByID to retrieve the COASegOpt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_COASegOpt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param SegmentNbr Desc: SegmentNbr   Required: True
      @param SegmentCode Desc: SegmentCode   Required: True   Allow empty value : True
      @param SubSegmentNbr Desc: SubSegmentNbr   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.COASegOptRow
   */  
export function get_COASegOpts_Company_COACode_SegmentNbr_SegmentCode_SubSegmentNbr(Company:string, COACode:string, SegmentNbr:string, SegmentCode:string, SubSegmentNbr:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_COASegOptRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/COASegOpts(" + Company + "," + COACode + "," + SegmentNbr + "," + SegmentCode + "," + SubSegmentNbr + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_COASegOptRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update COASegOpt for the service
   Description: Calls UpdateExt to update COASegOpt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_COASegOpt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param SegmentNbr Desc: SegmentNbr   Required: True
      @param SegmentCode Desc: SegmentCode   Required: True   Allow empty value : True
      @param SubSegmentNbr Desc: SubSegmentNbr   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.COASegOptRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_COASegOpts_Company_COACode_SegmentNbr_SegmentCode_SubSegmentNbr(Company:string, COACode:string, SegmentNbr:string, SegmentCode:string, SubSegmentNbr:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/COASegOpts(" + Company + "," + COACode + "," + SegmentNbr + "," + SegmentCode + "," + SubSegmentNbr + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete COASegOpt item
   Description: Call UpdateExt to delete COASegOpt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_COASegOpt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param SegmentNbr Desc: SegmentNbr   Required: True
      @param SegmentCode Desc: SegmentCode   Required: True   Allow empty value : True
      @param SubSegmentNbr Desc: SubSegmentNbr   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_COASegOpts_Company_COACode_SegmentNbr_SegmentCode_SubSegmentNbr(Company:string, COACode:string, SegmentNbr:string, SegmentCode:string, SubSegmentNbr:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/COASegOpts(" + Company + "," + COACode + "," + SegmentNbr + "," + SegmentCode + "," + SubSegmentNbr + ")", {
          method: 'delete',
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
   Summary: Calls GetRows for the service
   Description: Get COASegRes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_COASegRes
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.COASegResRow
   */  
export function get_COASegRes(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COASegResRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/COASegRes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COASegResRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_COASegRes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.COASegResRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.COASegResRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_COASegRes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/COASegRes", {
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
   Summary: Calls GetByID to retrieve the COASegRe item
   Description: Calls GetByID to retrieve the COASegRe item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_COASegRe
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param SegmentNbr Desc: SegmentNbr   Required: True
      @param SegmentCode Desc: SegmentCode   Required: True   Allow empty value : True
      @param RestrictID Desc: RestrictID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.COASegResRow
   */  
export function get_COASegRes_Company_COACode_SegmentNbr_SegmentCode_RestrictID(Company:string, COACode:string, SegmentNbr:string, SegmentCode:string, RestrictID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_COASegResRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/COASegRes(" + Company + "," + COACode + "," + SegmentNbr + "," + SegmentCode + "," + RestrictID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_COASegResRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update COASegRe for the service
   Description: Calls UpdateExt to update COASegRe. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_COASegRe
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param SegmentNbr Desc: SegmentNbr   Required: True
      @param SegmentCode Desc: SegmentCode   Required: True   Allow empty value : True
      @param RestrictID Desc: RestrictID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.COASegResRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_COASegRes_Company_COACode_SegmentNbr_SegmentCode_RestrictID(Company:string, COACode:string, SegmentNbr:string, SegmentCode:string, RestrictID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/COASegRes(" + Company + "," + COACode + "," + SegmentNbr + "," + SegmentCode + "," + RestrictID + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete COASegRe item
   Description: Call UpdateExt to delete COASegRe item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_COASegRe
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param SegmentNbr Desc: SegmentNbr   Required: True
      @param SegmentCode Desc: SegmentCode   Required: True   Allow empty value : True
      @param RestrictID Desc: RestrictID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_COASegRes_Company_COACode_SegmentNbr_SegmentCode_RestrictID(Company:string, COACode:string, SegmentNbr:string, SegmentCode:string, RestrictID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/COASegRes(" + Company + "," + COACode + "," + SegmentNbr + "," + SegmentCode + "," + RestrictID + ")", {
          method: 'delete',
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
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.COASegValuesListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COASegValuesListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COASegValuesListRow)
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
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseCOASegValues:string, whereClauseCOASegAcct:string, whereClauseCOASegOpt:string, whereClauseCOASegRes:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseCOASegValues!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCOASegValues=" + whereClauseCOASegValues
   }
   if(typeof whereClauseCOASegAcct!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCOASegAcct=" + whereClauseCOASegAcct
   }
   if(typeof whereClauseCOASegOpt!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCOASegOpt=" + whereClauseCOASegOpt
   }
   if(typeof whereClauseCOASegRes!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCOASegRes=" + whereClauseCOASegRes
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/GetRows" + params, {
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

   /**  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(coACode:string, segmentNbr:string, segmentCode:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof coACode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "coACode=" + coACode
   }
   if(typeof segmentNbr!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "segmentNbr=" + segmentNbr
   }
   if(typeof segmentCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "segmentCode=" + segmentCode
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/GetByID" + params, {
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

   /**  
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      @param whereClause Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      @param pageSize Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      @param absolutePage Desc: Page of rows to return.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/GetList" + params, {
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

   /**  
   Summary: Invoke method ChangeRevalueOpt
   Description: On Revalue Option change
   OperationID: ChangeRevalueOpt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRevalueOpt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRevalueOpt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeRevalueOpt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/ChangeRevalueOpt", {
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
   Summary: Invoke method ChangeRateType
   Description: On Rate Type changing
   OperationID: ChangeRateType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRateType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRateType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeRateType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/ChangeRateType", {
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
   Summary: Invoke method ChangeAccountContext
   Description: On Account context changing
   OperationID: ChangeAccountContext
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeAccountContext_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeAccountContext_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeAccountContext(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/ChangeAccountContext", {
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
   Summary: Invoke method ChangeAllowed
   Description: On allowed change this method evaluates the Currency account type option to handle proper functionality.
   OperationID: ChangeAllowed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeAllowed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeAllowed_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeAllowed(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/ChangeAllowed", {
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
   Summary: Invoke method ChangeCategory
   Description: This method convert the document currency to the journal currency.
   OperationID: ChangeCategory
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCategory_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCategory_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCategory(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/ChangeCategory", {
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
   Summary: Invoke method ChangeCurrencyAccount
   Description: On currency account change, all related currencies should be updated to allowed/not allowed
   OperationID: ChangeCurrencyAccount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCurrencyAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCurrencyAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCurrencyAccount(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/ChangeCurrencyAccount", {
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
   Summary: Invoke method ChangeSegvalue
   OperationID: ChangeSegvalue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeSegvalue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSegvalue_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeSegvalue(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/ChangeSegvalue", {
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
   Summary: Invoke method CheckForDupSegOpt
   Description: Purpose: Make sure a COASegment has not been entered twice for a given segment value.
The ipSubSegmentNbr is the sub segment number to look for in the COASegOpt table.
The segment number to search on is one since these options are only valid for the
natural account and the natural account is ALWAYS segment number 1.
Parameters:
<param name="ipCOACode"> COA Code</param><param name="ipSubSegmentNbr"> Segment Number to check for existence</param><param name="ipSegmentCode">Segment Code to search for </param>
Notes:
   OperationID: CheckForDupSegOpt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckForDupSegOpt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckForDupSegOpt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckForDupSegOpt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/CheckForDupSegOpt", {
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
   Summary: Invoke method ChangeStatistical
   OperationID: ChangeStatistical
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeStatistical_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeStatistical_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeStatistical(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/ChangeStatistical", {
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
   Summary: Invoke method ChangeStatisticalOnly
   OperationID: ChangeStatisticalOnly
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeStatisticalOnly_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeStatisticalOnly_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeStatisticalOnly(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/ChangeStatisticalOnly", {
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
   Summary: Invoke method ChangeStatUOMCode
   OperationID: ChangeStatUOMCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeStatUOMCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeStatUOMCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeStatUOMCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/ChangeStatUOMCode", {
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
   Summary: Invoke method ChangeLinkedPlant
   OperationID: ChangeLinkedPlant
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeLinkedPlant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeLinkedPlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeLinkedPlant(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/ChangeLinkedPlant", {
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
   Summary: Invoke method ChangeActive
   Description: Change Active related validations.
   OperationID: ChangeActive
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeActive_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeActive_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeActive(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/ChangeActive", {
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
   Summary: Invoke method COASegValueActiveFlagChanging
   Description: Performs validations when changing ActiveFlag
Checks for GL Control references when marking a segment value as inactive
   OperationID: COASegValueActiveFlagChanging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/COASegValueActiveFlagChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/COASegValueActiveFlagChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_COASegValueActiveFlagChanging(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/COASegValueActiveFlagChanging", {
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
   Summary: Invoke method RemoveSiteSegmentCodeDuplicate
   Description: SegmentCode duplicate values should be removed.
   OperationID: RemoveSiteSegmentCodeDuplicate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RemoveSiteSegmentCodeDuplicate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RemoveSiteSegmentCodeDuplicate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RemoveSiteSegmentCodeDuplicate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/RemoveSiteSegmentCodeDuplicate", {
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
   Summary: Invoke method ChangeSiteSegmentCode
   Description: Validates new Site Segment Code value
   OperationID: ChangeSiteSegmentCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeSiteSegmentCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSiteSegmentCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeSiteSegmentCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/ChangeSiteSegmentCode", {
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
   Summary: Invoke method SiteSegmentChanged
   Description: Populates info about selected segment value
   OperationID: SiteSegmentChanged
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SiteSegmentChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SiteSegmentChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SiteSegmentChanged(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/SiteSegmentChanged", {
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
   Summary: Invoke method ChgStatUOMCode
   OperationID: ChgStatUOMCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChgStatUOMCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChgStatUOMCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChgStatUOMCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/ChgStatUOMCode", {
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
   Summary: Invoke method GetCOASegmentGlobalFields
   Description: none
   OperationID: GetCOASegmentGlobalFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCOASegmentGlobalFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCOASegmentGlobalFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCOASegmentGlobalFields(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/GetCOASegmentGlobalFields", {
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
   Summary: Invoke method ComboValues
   Description: Purpose:Used to setup the initial values of the combos placed on the Header
            
Parameters:
<param name="opCOACode">Indicates the COACODE the Chart of Accounts</param><param name="opDescription">Indicates the Description on fo the COACODE</param><param name="opSegmentNbr">Indicates Segment number of the Segment</param><param name="opSegmentName">Indicates the Segment Name of the Segment</param><param name="opGlobalCOA">opGlobalCOA</param><param name="opGlobalSegment">opGlobalSegment </param>
Notes:
   OperationID: ComboValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ComboValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ComboValues(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/ComboValues", {
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
   Summary: Invoke method ValidateCOACodeSite
   Description: returns a description and Global COA flags of the entered COA code with Site Segment info
   OperationID: ValidateCOACodeSite
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateCOACodeSite_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateCOACodeSite_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateCOACodeSite(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/ValidateCOACodeSite", {
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
   Summary: Invoke method ValidateCOACode
   Description: returns a description and Global COA flags of the entered COA code
   OperationID: ValidateCOACode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateCOACode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateCOACode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateCOACode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/ValidateCOACode", {
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
   Summary: Invoke method ValidateCOASegment
   Description: Validate segment number
   OperationID: ValidateCOASegment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateCOASegment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateCOASegment_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateCOASegment(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/ValidateCOASegment", {
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
   Summary: Invoke method GetListCBOnly
   Description: Purpose:
Parameters:
<param name="WhereClause">COASegValues search clause</param><param name="pageSize">Page size</param><param name="absolutePage">Absolute page</param><param name="morePages">More Pages</param>
Notes:
   OperationID: GetListCBOnly
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListCBOnly_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListCBOnly_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListCBOnly(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/GetListCBOnly", {
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
   Summary: Invoke method ValidateCurrencyAccount
   Description: Purpose:
Parameters:
<param name="ipCOACode">COA code</param><param name="ipSegmentCode">segment code</param><param name="ipCurrencyAcct">flag identifying the segment as a currency account</param><param name="CurrencyAcctType">currency account Type</param>
Notes:
   OperationID: ValidateCurrencyAccount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateCurrencyAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateCurrencyAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateCurrencyAccount(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/ValidateCurrencyAccount", {
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
   Summary: Invoke method ValidateDefaultSegment
   Description: Purpose:
Parameters:
<param name="ipCOACode"> COA Code</param><param name="ipSubSegmentNbr"> Segment Number to check for existence</param><param name="ipSegmentCode">Segment Code to search for </param>
Notes:
   OperationID: ValidateDefaultSegment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateDefaultSegment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateDefaultSegment_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateDefaultSegment(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/ValidateDefaultSegment", {
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
   Summary: Invoke method DefaultsOnAdd
   Description: Set Default creating a new account
   OperationID: DefaultsOnAdd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultsOnAdd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultsOnAdd_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DefaultsOnAdd(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/DefaultsOnAdd", {
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
   Summary: Invoke method DefaultsOnAddSegAcct
   Description: Set Default creating a new COASegAcct
   OperationID: DefaultsOnAddSegAcct
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultsOnAddSegAcct_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultsOnAddSegAcct_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DefaultsOnAddSegAcct(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/DefaultsOnAddSegAcct", {
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
   Summary: Invoke method DeleteTransactionCurrencies
   Description: Delete Transaction Currencies
   OperationID: DeleteTransactionCurrencies
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteTransactionCurrencies_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteTransactionCurrencies_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteTransactionCurrencies(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/DeleteTransactionCurrencies", {
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
   Summary: Invoke method IsStatOnlySegment
   OperationID: IsStatOnlySegment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsStatOnlySegment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsStatOnlySegment_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IsStatOnlySegment(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/IsStatOnlySegment", {
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
   Summary: Invoke method getBookRevOpt
   OperationID: getBookRevOpt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/getBookRevOpt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/getBookRevOpt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_getBookRevOpt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/getBookRevOpt", {
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
   Summary: Invoke method CheckCOASeparatorInSegmentValue
   Description: Return warning message if Segment Value contains COA Separator
   OperationID: CheckCOASeparatorInSegmentValue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckCOASeparatorInSegmentValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCOASeparatorInSegmentValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckCOASeparatorInSegmentValue(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/CheckCOASeparatorInSegmentValue", {
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
   Summary: Invoke method GenerateSiteSegmentSetupData
   OperationID: GenerateSiteSegmentSetupData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateSiteSegmentSetupData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateSiteSegmentSetupData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenerateSiteSegmentSetupData(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/GenerateSiteSegmentSetupData", {
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
   Summary: Invoke method GetSiteSetting
   Description: Site Segment wizard availability
   OperationID: GetSiteSetting
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSiteSetting_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSiteSetting_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSiteSetting(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/GetSiteSetting", {
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
   Summary: Invoke method DefaultBookID
   Description: Returns the default book value.
   OperationID: DefaultBookID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultBookID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultBookID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DefaultBookID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/DefaultBookID", {
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
   Summary: Invoke method GetInterSiteAccountPairs
   Description: Returns intersite account pairs for due from/due to
   OperationID: GetInterSiteAccountPairs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInterSiteAccountPairs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInterSiteAccountPairs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetInterSiteAccountPairs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/GetInterSiteAccountPairs", {
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
   Summary: Invoke method IntersiteAccountPairsApply
   Description: Apply due from/due to account pairs
   OperationID: IntersiteAccountPairsApply
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IntersiteAccountPairsApply_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IntersiteAccountPairsApply_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IntersiteAccountPairsApply(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/IntersiteAccountPairsApply", {
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
   Summary: Invoke method GetSiteSegmentSetupData
   Description: Generates data for Site Segment Setup Wizard
   OperationID: GetSiteSegmentSetupData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSiteSegmentSetupData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSiteSegmentSetupData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSiteSegmentSetupData(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/GetSiteSegmentSetupData", {
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
   Summary: Invoke method SiteSegmentSetupApply
   Description: Applies Site Segment info for segment values
   OperationID: SiteSegmentSetupApply
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SiteSegmentSetupApply_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SiteSegmentSetupApply_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SiteSegmentSetupApply(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/SiteSegmentSetupApply", {
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
   Summary: Invoke method GetNewCOASegValues
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCOASegValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCOASegValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCOASegValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCOASegValues(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/GetNewCOASegValues", {
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
   Summary: Invoke method GetNewCOASegAcct
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCOASegAcct
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCOASegAcct_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCOASegAcct_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCOASegAcct(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/GetNewCOASegAcct", {
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
   Summary: Invoke method GetNewCOASegOpt
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCOASegOpt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCOASegOpt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCOASegOpt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCOASegOpt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/GetNewCOASegOpt", {
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
   Summary: Invoke method GetNewCOASegRes
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCOASegRes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCOASegRes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCOASegRes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCOASegRes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/GetNewCOASegRes", {
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
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteByID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/DeleteByID", {
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
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/GetBySysRowID" + params, {
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

   /**  
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/GetBySysRowIDs" + params, {
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

   /**  
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
   OperationID: Update
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Update(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/Update", {
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
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateExt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COASegAcctRow{
   "odatametadata":string,
   "value":Erp_Tablesets_COASegAcctRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COASegOptRow{
   "odatametadata":string,
   "value":Erp_Tablesets_COASegOptRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COASegResRow{
   "odatametadata":string,
   "value":Erp_Tablesets_COASegResRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COASegValuesListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_COASegValuesListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COASegValuesRow{
   "odatametadata":string,
   "value":Erp_Tablesets_COASegValuesRow[],
}

export interface Erp_Tablesets_COASegAcctRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  System generated number from 1 through 20.  */  
   "SegmentNbr":number,
      /**  Segment value used to construct the GL Account.  */  
   "SegmentCode":string,
      /**  Unique code identifying the currency.  Only those values defined in the CurrencyMaster are allowed.  */  
   "CurrencyCode":string,
      /**  Indicates the currency can be used as a transactional currency.  */  
   "Allowed":boolean,
      /**   Indicates if the transaction currency amount can be revalued.  Valid values are:
0 - no revalulation (deafult)
1 - only profits
2 - only losses
3 - both profit and losses  */  
   "Revalue":number,
      /**  The natural account used for booking currency gains.  */  
   "GainAccount":string,
      /**  The natural account used for booking currency losses.  */  
   "LossAccount":string,
      /**  The natural account used as the accrual account.  */  
   "AccrualAccount":string,
      /**  GainSegVal1  */  
   "GainSegVal1":string,
      /**  GainSegVal2  */  
   "GainSegVal2":string,
      /**  GainSegVal3  */  
   "GainSegVal3":string,
      /**  GainSegVal4  */  
   "GainSegVal4":string,
      /**  GainSegVal5  */  
   "GainSegVal5":string,
      /**  GainSegVal6  */  
   "GainSegVal6":string,
      /**  GainSegVal7  */  
   "GainSegVal7":string,
      /**  GainSegVal8  */  
   "GainSegVal8":string,
      /**  GainSegVal9  */  
   "GainSegVal9":string,
      /**  GainSegVal10  */  
   "GainSegVal10":string,
      /**  GainSegVal11  */  
   "GainSegVal11":string,
      /**  GainSegVal12  */  
   "GainSegVal12":string,
      /**  GainSegVal13  */  
   "GainSegVal13":string,
      /**  GainSegVal14  */  
   "GainSegVal14":string,
      /**  GainSegVal15  */  
   "GainSegVal15":string,
      /**  GainSegVal16  */  
   "GainSegVal16":string,
      /**  GainSegVal17  */  
   "GainSegVal17":string,
      /**  GainSegVal18  */  
   "GainSegVal18":string,
      /**  GainSegVal19  */  
   "GainSegVal19":string,
      /**  GainSegVal20  */  
   "GainSegVal20":string,
      /**  LossSegVal1  */  
   "LossSegVal1":string,
      /**  LossSegVal2  */  
   "LossSegVal2":string,
      /**  LossSegVal3  */  
   "LossSegVal3":string,
      /**  LossSegVal4  */  
   "LossSegVal4":string,
      /**  LossSegVal5  */  
   "LossSegVal5":string,
      /**  LossSegVal6  */  
   "LossSegVal6":string,
      /**  LossSegVal7  */  
   "LossSegVal7":string,
      /**  LossSegVal8  */  
   "LossSegVal8":string,
      /**  LossSegVal9  */  
   "LossSegVal9":string,
      /**  LossSegVal10  */  
   "LossSegVal10":string,
      /**  LossSegVal11  */  
   "LossSegVal11":string,
      /**  LossSegVal12  */  
   "LossSegVal12":string,
      /**  LossSegVal13  */  
   "LossSegVal13":string,
      /**  LossSegVal14  */  
   "LossSegVal14":string,
      /**  LossSegVal15  */  
   "LossSegVal15":string,
      /**  LossSegVal16  */  
   "LossSegVal16":string,
      /**  LossSegVal17  */  
   "LossSegVal17":string,
      /**  LossSegVal18  */  
   "LossSegVal18":string,
      /**  LossSegVal19  */  
   "LossSegVal19":string,
      /**  LossSegVal20  */  
   "LossSegVal20":string,
      /**  AccrualSegVal1  */  
   "AccrualSegVal1":string,
      /**  AccrualSegVal2  */  
   "AccrualSegVal2":string,
      /**  AccrualSegVal3  */  
   "AccrualSegVal3":string,
      /**  AccrualSegVal4  */  
   "AccrualSegVal4":string,
      /**  AccrualSegVal5  */  
   "AccrualSegVal5":string,
      /**  AccrualSegVal6  */  
   "AccrualSegVal6":string,
      /**  AccrualSegVal7  */  
   "AccrualSegVal7":string,
      /**  AccrualSegVal8  */  
   "AccrualSegVal8":string,
      /**  AccrualSegVal9  */  
   "AccrualSegVal9":string,
      /**  AccrualSegVal10  */  
   "AccrualSegVal10":string,
      /**  AccrualSegVal11  */  
   "AccrualSegVal11":string,
      /**  AccrualSegVal12  */  
   "AccrualSegVal12":string,
      /**  AccrualSegVal13  */  
   "AccrualSegVal13":string,
      /**  AccrualSegVal14  */  
   "AccrualSegVal14":string,
      /**  AccrualSegVal15  */  
   "AccrualSegVal15":string,
      /**  AccrualSegVal16  */  
   "AccrualSegVal16":string,
      /**  AccrualSegVal17  */  
   "AccrualSegVal17":string,
      /**  AccrualSegVal18  */  
   "AccrualSegVal18":string,
      /**  AccrualSegVal19  */  
   "AccrualSegVal19":string,
      /**  AccrualSegVal20  */  
   "AccrualSegVal20":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Accrual GL Account description  */  
   "AccrualGLDesc":string,
      /**  Gain GL Account Description  */  
   "GainGLDesc":string,
      /**  Loss GL Account Description  */  
   "LossGLDesc":string,
   "BitFlag":number,
   "CurrencyCurrencyID":string,
   "CurrencyCurrDesc":string,
   "CurrencyDocumentDesc":string,
   "CurrencyCurrName":string,
   "CurrencyCurrSymbol":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_COASegOptRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  System generated number from 1 through 20.  */  
   "SegmentNbr":number,
      /**  Segment value used to construct the GL Account.  */  
   "SegmentCode":string,
      /**  System generated sequence number  */  
   "SubSegmentNbr":number,
      /**   Indicates if a segment is used for the natural account.  Valid values are:
M - Mandatory
O - Optional
N - Not Used  */  
   "ValOption":string,
      /**  Indicates the default segment value to be used for this natural account.  */  
   "DefaultSegment":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
   "COASegmentSegmentName":string,
   "COASubSegmentSegmentName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_COASegResRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  System generated number from 1 through 20.  */  
   "SegmentNbr":number,
      /**  Segment value used to construct the GL Account.  */  
   "SegmentCode":string,
      /**  Application DLL name  */  
   "RestrictID":string,
      /**  Application name text.  */  
   "RestrictText":string,
      /**  Indicates if GL Account entry is prohibited  */  
   "FctBlocked":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_COASegValuesListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  System generated number from 1 through 20.  */  
   "SegmentNbr":number,
      /**  Segment value used to construct the GL Account.  */  
   "SegmentCode":string,
      /**  Name of Segment Value  */  
   "SegmentName":string,
      /**  Segment description.  */  
   "SegmentDesc":string,
      /**  Short name of the segment value.  */  
   "SegmentAbbrev":string,
      /**  Indicates if the segment is active.  Transactions cannot be posted to inactive segments.  */  
   "ActiveFlag":boolean,
      /**  Date the segment begins to be used.  It must be less than or equal to the EffectiveTo date.  */  
   "EffectiveFrom":string,
      /**  Date the segment is no longer used.  It must be greater than or equal to the EffectiveFrom date, if a value was entered in that field.  */  
   "EffectiveTo":string,
      /**  Required for the Natrual Account (segment number 1). Identifies the account category that is used to determine other characteristics.  */  
   "Category":string,
      /**  Indicates if the account is a debit or credit and is only valid for the natural account (segment 1).  Valid values are D for Debit and C for Credit.  */  
   "NormalBalance":string,
      /**  Rate type used for debit balances.  */  
   "DebitRateType":string,
      /**  Rate type used for credit balances  */  
   "CreditRateType":string,
      /**  Curency Account  */  
   "CurrAcct":boolean,
      /**  Reference Entity type assigned to this COASegValue.  Only valid when the COASegment.RefEntity = "GLCOARefType".  */  
   "RefEntityType":string,
      /**   0)      Summarize (default)
1)      Summarize debit and credits separately
2)      No summarization  */  
   "Summarization":number,
      /**  This flag determines if journal detail records with this natural account are allowed to be matched.  */  
   "MatchingEnabled":boolean,
      /**   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  */  
   "Statistical":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Identifies the account category this is used to determine characteristics when the segment value is reversed.  */  
   "ReverseCategory":string,
      /**  CurrencyAcctType  */  
   "CurrencyAcctType":string,
      /**  RevalueOpt  */  
   "RevalueOpt":number,
      /**  COSegDtlNbr  */  
   "COSegDtlNbr":number,
      /**  COPrintBalanceInvDtl  */  
   "COPrintBalanceInvDtl":boolean,
      /**  Logical indicating if this chart has been used.  */  
   "ChartInUse":boolean,
      /**  Logical indicating if this segment value has been used.  */  
   "SegValInUse":boolean,
      /**  Logical indicating whether or not the COA has a segment defined as 'entry control' equal to natural account and controls whether or not a segment option record can be entered for a natural account value.  */  
   "SegWithSegOneControl":boolean,
      /**  Logical indicating if the reference type is required for this segment value  */  
   "RefTypeRqd":boolean,
      /**  Segment number name from the COASegment table.  Used for display purposes in segment value searches where more than one segment number is searched at a time.  */  
   "SegNbrName":string,
   "ReverseCategoryDescription":string,
      /**  Text describing this category  */  
   "CategoryIDDescription":string,
      /**  Description  */  
   "CreditRateGrpDescription":string,
      /**  Description  */  
   "DebitRateGrpDescription":string,
      /**  Description of the Reference type  */  
   "GLCOARefTypeRefTypeDesc":string,
   "StatisticalDesc":string,
   "EffectiveRevalueOpt":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_COASegValuesRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  System generated number from 1 through 20.  */  
   "SegmentNbr":number,
      /**  Segment value used to construct the GL Account.  */  
   "SegmentCode":string,
      /**  Name of Segment Value  */  
   "SegmentName":string,
      /**  Segment description.  */  
   "SegmentDesc":string,
      /**  Short name of the segment value.  */  
   "SegmentAbbrev":string,
      /**  Indicates if the segment is active.  Transactions cannot be posted to inactive segments.  */  
   "ActiveFlag":boolean,
      /**  Date the segment begins to be used.  It must be less than or equal to the EffectiveTo date.  */  
   "EffectiveFrom":string,
      /**  Date the segment is no longer used.  It must be greater than or equal to the EffectiveFrom date, if a value was entered in that field.  */  
   "EffectiveTo":string,
      /**  Required for the Natrual Account (segment number 1). Identifies the account category that is used to determine other characteristics.  */  
   "Category":string,
      /**  Indicates if the account is a debit or credit and is only valid for the natural account (segment 1).  Valid values are D for Debit and C for Credit.  */  
   "NormalBalance":string,
      /**  Rate type used for debit balances.  */  
   "DebitRateType":string,
      /**  Rate type used for credit balances  */  
   "CreditRateType":string,
      /**  Curency Account  */  
   "CurrAcct":boolean,
      /**  Reference Entity type assigned to this COASegValue.  Only valid when the COASegment.RefEntity = "GLCOARefType".  */  
   "RefEntityType":string,
      /**   0)      Summarize (default)
1)      Summarize debit and credits separately
2)      No summarization  */  
   "Summarization":number,
      /**  This flag determines if journal detail records with this natural account are allowed to be matched.  */  
   "MatchingEnabled":boolean,
      /**   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  */  
   "Statistical":number,
      /**  StatUOMCode  */  
   "StatUOMCode":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Identifies the account category this is used to determine characteristics when the segment value is reversed.  */  
   "ReverseCategory":string,
      /**  External financial analysis code linked to the natural account.  */  
   "ExtAnalysisCode":string,
      /**  CurrencyAcctType  */  
   "CurrencyAcctType":string,
      /**  RevalueOpt  */  
   "RevalueOpt":number,
      /**  GLGainAcctContext  */  
   "GLGainAcctContext":string,
      /**  GLLossAcctContext  */  
   "GLLossAcctContext":string,
      /**  GainAccount  */  
   "GainAccount":string,
      /**  LossAccount  */  
   "LossAccount":string,
      /**  AccrualAccount  */  
   "AccrualAccount":string,
      /**  GainSegVal1  */  
   "GainSegVal1":string,
      /**  GainSegVal2  */  
   "GainSegVal2":string,
      /**  GainSegVal3  */  
   "GainSegVal3":string,
      /**  GainSegVal4  */  
   "GainSegVal4":string,
      /**  GainSegVal5  */  
   "GainSegVal5":string,
      /**  GainSegVal6  */  
   "GainSegVal6":string,
      /**  GainSegVal7  */  
   "GainSegVal7":string,
      /**  GainSegVal8  */  
   "GainSegVal8":string,
      /**  GainSegVal9  */  
   "GainSegVal9":string,
      /**  GainSegVal10  */  
   "GainSegVal10":string,
      /**  GainSegVal11  */  
   "GainSegVal11":string,
      /**  GainSegVal12  */  
   "GainSegVal12":string,
      /**  GainSegVal13  */  
   "GainSegVal13":string,
      /**  GainSegVal14  */  
   "GainSegVal14":string,
      /**  GainSegVal15  */  
   "GainSegVal15":string,
      /**  GainSegVal16  */  
   "GainSegVal16":string,
      /**  GainSegVal17  */  
   "GainSegVal17":string,
      /**  GainSegVal18  */  
   "GainSegVal18":string,
      /**  GainSegVal19  */  
   "GainSegVal19":string,
      /**  GainSegVal20  */  
   "GainSegVal20":string,
      /**  LossSegVal1  */  
   "LossSegVal1":string,
      /**  LossSegVal2  */  
   "LossSegVal2":string,
      /**  LossSegVal3  */  
   "LossSegVal3":string,
      /**  LossSegVal4  */  
   "LossSegVal4":string,
      /**  LossSegVal5  */  
   "LossSegVal5":string,
      /**  LossSegVal6  */  
   "LossSegVal6":string,
      /**  LossSegVal7  */  
   "LossSegVal7":string,
      /**  LossSegVal8  */  
   "LossSegVal8":string,
      /**  LossSegVal9  */  
   "LossSegVal9":string,
      /**  LossSegVal10  */  
   "LossSegVal10":string,
      /**  LossSegVal11  */  
   "LossSegVal11":string,
      /**  LossSegVal12  */  
   "LossSegVal12":string,
      /**  LossSegVal13  */  
   "LossSegVal13":string,
      /**  LossSegVal14  */  
   "LossSegVal14":string,
      /**  LossSegVal15  */  
   "LossSegVal15":string,
      /**  LossSegVal16  */  
   "LossSegVal16":string,
      /**  LossSegVal17  */  
   "LossSegVal17":string,
      /**  LossSegVal18  */  
   "LossSegVal18":string,
      /**  LossSegVal19  */  
   "LossSegVal19":string,
      /**  LossSegVal20  */  
   "LossSegVal20":string,
      /**  AccrualSegVal1  */  
   "AccrualSegVal1":string,
      /**  AccrualSegVal2  */  
   "AccrualSegVal2":string,
      /**  AccrualSegVal3  */  
   "AccrualSegVal3":string,
      /**  AccrualSegVal4  */  
   "AccrualSegVal4":string,
      /**  AccrualSegVal5  */  
   "AccrualSegVal5":string,
      /**  AccrualSegVal6  */  
   "AccrualSegVal6":string,
      /**  AccrualSegVal7  */  
   "AccrualSegVal7":string,
      /**  AccrualSegVal8  */  
   "AccrualSegVal8":string,
      /**  AccrualSegVal9  */  
   "AccrualSegVal9":string,
      /**  AccrualSegVal10  */  
   "AccrualSegVal10":string,
      /**  AccrualSegVal11  */  
   "AccrualSegVal11":string,
      /**  AccrualSegVal12  */  
   "AccrualSegVal12":string,
      /**  AccrualSegVal13  */  
   "AccrualSegVal13":string,
      /**  AccrualSegVal14  */  
   "AccrualSegVal14":string,
      /**  AccrualSegVal15  */  
   "AccrualSegVal15":string,
      /**  AccrualSegVal16  */  
   "AccrualSegVal16":string,
      /**  AccrualSegVal17  */  
   "AccrualSegVal17":string,
      /**  AccrualSegVal18  */  
   "AccrualSegVal18":string,
      /**  AccrualSegVal19  */  
   "AccrualSegVal19":string,
      /**  AccrualSegVal20  */  
   "AccrualSegVal20":string,
      /**  COSegDtlNbr  */  
   "COSegDtlNbr":number,
      /**  COPrintBalanceInvDtl  */  
   "COPrintBalanceInvDtl":boolean,
      /**  Non-Admissible Expense Code (CSF Belgium)  */  
   "BENAEID":string,
      /**  Mapped  */  
   "Mapped":boolean,
      /**  One of the UD codes having a CodeTypeID equal to GLRepCat. Or, if GLRepCat does not exist, then it may be free text.  */  
   "ReportCategory":string,
      /**  ReverseReportCategory  */  
   "ReverseReportCategory":string,
      /**  LinkedPlant  */  
   "LinkedPlant":string,
      /**  Accrual Account Description  */  
   "AccrualAcctDesc":string,
      /**  Gain Account Description  */  
   "GainAcctDesc":string,
   "GlbValuesFlag":boolean,
   "GlobalSegValues":boolean,
   "GlobalSegValuesLock":boolean,
      /**  Loss Account Description  */  
   "LossAcctDesc":string,
      /**  Internal logical used by UI that indicates if GLAccounts exist for this COA and that the display gl account must be rebuilt  */  
   "RebuildGLAccts":boolean,
      /**  Logical indicating if the reference type is required for this segment value  */  
   "RefTypeRqd":boolean,
   "ReverseCategoryDescription":string,
      /**  Segment number name from the COASegment table.  Used for display purposes in segment value searches where more than one segment number is searched at a time.  */  
   "SegNbrName":string,
      /**  Logical indicating if this segment value has been used.  */  
   "SegValInUse":boolean,
      /**  Logical indicating whether or not the COA has a segment defined as 'entry control' equal to natural account and controls whether or not a segment option record can be entered for a natural account value.  */  
   "SegWithSegOneControl":boolean,
   "StatisticalDesc":string,
      /**  Logical indicating if this chart has been used.  */  
   "ChartInUse":boolean,
   "BitFlag":number,
   "CategoryIDDescription":string,
   "COASegmentSiteSegment":boolean,
   "COASegmentSegmentName":string,
   "COSegDtlSegmentName":string,
   "CreditRateGrpDescription":string,
   "DebitRateGrpDescription":string,
   "GLCOARefTypeRefTypeDesc":string,
      /**  RowMod  */  
   "RowMod":string,
   "UD_SysRevID":string,
   "BudgetSegCode_c":string,
   "BudgetReportGroup_c":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param proposedActiveFlag
      @param ds
   */  
export interface COASegValueActiveFlagChanging_input{
      /**  Proposed ActiveFlag value  */  
   proposedActiveFlag:boolean,
   ds:Erp_Tablesets_COASegValuesTableset[],
}

export interface COASegValueActiveFlagChanging_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_COASegValuesTableset[],
   msgInActive:string,
   msgActive:string,
}
}

   /** Required : 
      @param context
   */  
export interface ChangeAccountContext_input{
   context:string,
}

export interface ChangeAccountContext_output{
}

   /** Required : 
      @param active
      @param ds
   */  
export interface ChangeActive_input{
   active:boolean,
   ds:Erp_Tablesets_COASegValuesTableset[],
}

export interface ChangeActive_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_COASegValuesTableset[],
   msgInActive:string,
   msgActive:string,
}
}

   /** Required : 
      @param proposedAllowed
      @param ipCOACode
      @param ipSegmentNbr
      @param ipSegmentCode
      @param ipCurrencyCode
      @param ds
   */  
export interface ChangeAllowed_input{
      /**  The proposed  Allowed value  */  
   proposedAllowed:boolean,
      /**  The proposed  Allowed value  */  
   ipCOACode:string,
      /**  The proposed  Allowed value  */  
   ipSegmentNbr:number,
      /**  The proposed  Allowed value  */  
   ipSegmentCode:string,
      /**  The proposed  Allowed value  */  
   ipCurrencyCode:string,
   ds:Erp_Tablesets_COASegValuesTableset[],
}

export interface ChangeAllowed_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_COASegValuesTableset[],
}
}

   /** Required : 
      @param proposedCategory
      @param ds
   */  
export interface ChangeCategory_input{
      /**  The proposed  Amount  */  
   proposedCategory:string,
   ds:Erp_Tablesets_COASegValuesTableset[],
}

export interface ChangeCategory_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_COASegValuesTableset[],
}
}

   /** Required : 
      @param ipValue
      @param ds
   */  
export interface ChangeCurrencyAccount_input{
      /**  Currency Account flag  */  
   ipValue:string,
   ds:Erp_Tablesets_COASegValuesTableset[],
}

export interface ChangeCurrencyAccount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_COASegValuesTableset[],
}
}

   /** Required : 
      @param linkedPlant
      @param ds
   */  
export interface ChangeLinkedPlant_input{
   linkedPlant:string,
   ds:Erp_Tablesets_COASegValuesTableset[],
}

export interface ChangeLinkedPlant_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_COASegValuesTableset[],
   msg:string,
   GLmsg:string,
}
}

   /** Required : 
      @param rateType
      @param isCredit
   */  
export interface ChangeRateType_input{
   rateType:string,
   isCredit:boolean,
}

export interface ChangeRateType_output{
}

   /** Required : 
      @param proposedRevalue
      @param ds
   */  
export interface ChangeRevalueOpt_input{
   proposedRevalue:number,
   ds:Erp_Tablesets_COASegValuesTableset[],
}

export interface ChangeRevalueOpt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_COASegValuesTableset[],
}
}

   /** Required : 
      @param ipValue
      @param ds
   */  
export interface ChangeSegvalue_input{
      /**  The proposed segment value  */  
   ipValue:string,
   ds:Erp_Tablesets_COASegValuesTableset[],
}

export interface ChangeSegvalue_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_COASegValuesTableset[],
}
}

   /** Required : 
      @param linkedPlant
      @param segmentCode
      @param ds
   */  
export interface ChangeSiteSegmentCode_input{
   linkedPlant:string,
   segmentCode:string,
   ds:Erp_Tablesets_SiteSegmentSetupTableset[],
}

export interface ChangeSiteSegmentCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SiteSegmentSetupTableset[],
   msg:string,
   GLmsg:string,
}
}

   /** Required : 
      @param statUOMCode
      @param ds
   */  
export interface ChangeStatUOMCode_input{
   statUOMCode:string,
   ds:Erp_Tablesets_COASegValuesTableset[],
}

export interface ChangeStatUOMCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_COASegValuesTableset[],
   msg:string,
}
}

   /** Required : 
      @param segmentCode
      @param coaCode
   */  
export interface ChangeStatisticalOnly_input{
   segmentCode:string,
   coaCode:string,
}

export interface ChangeStatisticalOnly_output{
}

   /** Required : 
      @param statistical
      @param ds
   */  
export interface ChangeStatistical_input{
   statistical:number,
   ds:Erp_Tablesets_COASegValuesTableset[],
}

export interface ChangeStatistical_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_COASegValuesTableset[],
   msg:string,
}
}

   /** Required : 
      @param coaCode
      @param segmentCode
   */  
export interface CheckCOASeparatorInSegmentValue_input{
      /**  COA Code  */  
   coaCode:string,
      /**  Segment Code  */  
   segmentCode:string,
}

export interface CheckCOASeparatorInSegmentValue_output{
parameters : {
      /**  output parameters  */  
   warnMessage:string,
}
}

   /** Required : 
      @param ipCOACode
      @param ipSubSegmentNbr
      @param ipSegmentCode
   */  
export interface CheckForDupSegOpt_input{
   ipCOACode:string,
   ipSubSegmentNbr:number,
   ipSegmentCode:string,
}

export interface CheckForDupSegOpt_output{
}

   /** Required : 
      @param statUOMCode
   */  
export interface ChgStatUOMCode_input{
      /**  statUOMCode  */  
   statUOMCode:string,
}

export interface ChgStatUOMCode_output{
}

export interface ComboValues_output{
parameters : {
      /**  output parameters  */  
   opCOACode:string,
   opDescription:string,
   opSegmentNbr:number,
   opSegmentName:string,
   opGlobalCOA:boolean,
   opGlobalSegment:boolean,
}
}

   /** Required : 
      @param coaCode
   */  
export interface DefaultBookID_input{
   coaCode:string,
}

export interface DefaultBookID_output{
   returnObj:string,
}

   /** Required : 
      @param ipGLAccount
      @param ipAccountDescField
      @param ds
   */  
export interface DefaultsOnAddSegAcct_input{
      /**  GL Account being added  */  
   ipGLAccount:string,
      /**  GL Account description field being updated  */  
   ipAccountDescField:string,
   ds:Erp_Tablesets_COASegValuesTableset[],
}

export interface DefaultsOnAddSegAcct_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_COASegValuesTableset[],
}
}

   /** Required : 
      @param ipGLAccount
      @param ipAccountField
      @param ds
   */  
export interface DefaultsOnAdd_input{
      /**  GL Account being added  */  
   ipGLAccount:string,
      /**  GL Account description field being updated  */  
   ipAccountField:string,
   ds:Erp_Tablesets_COASegValuesTableset[],
}

export interface DefaultsOnAdd_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_COASegValuesTableset[],
}
}

   /** Required : 
      @param coACode
      @param segmentNbr
      @param segmentCode
   */  
export interface DeleteByID_input{
   coACode:string,
   segmentNbr:number,
   segmentCode:string,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param ipCOACode
      @param ipSegmentNbr
      @param ipSegmentCode
      @param ds
   */  
export interface DeleteTransactionCurrencies_input{
   ipCOACode:string,
   ipSegmentNbr:number,
   ipSegmentCode:string,
   ds:Erp_Tablesets_COASegValuesTableset[],
}

export interface DeleteTransactionCurrencies_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_COASegValuesTableset[],
}
}

export interface Erp_Tablesets_COASegAcctRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  System generated number from 1 through 20.  */  
   SegmentNbr:number,
      /**  Segment value used to construct the GL Account.  */  
   SegmentCode:string,
      /**  Unique code identifying the currency.  Only those values defined in the CurrencyMaster are allowed.  */  
   CurrencyCode:string,
      /**  Indicates the currency can be used as a transactional currency.  */  
   Allowed:boolean,
      /**   Indicates if the transaction currency amount can be revalued.  Valid values are:
0 - no revalulation (deafult)
1 - only profits
2 - only losses
3 - both profit and losses  */  
   Revalue:number,
      /**  The natural account used for booking currency gains.  */  
   GainAccount:string,
      /**  The natural account used for booking currency losses.  */  
   LossAccount:string,
      /**  The natural account used as the accrual account.  */  
   AccrualAccount:string,
      /**  GainSegVal1  */  
   GainSegVal1:string,
      /**  GainSegVal2  */  
   GainSegVal2:string,
      /**  GainSegVal3  */  
   GainSegVal3:string,
      /**  GainSegVal4  */  
   GainSegVal4:string,
      /**  GainSegVal5  */  
   GainSegVal5:string,
      /**  GainSegVal6  */  
   GainSegVal6:string,
      /**  GainSegVal7  */  
   GainSegVal7:string,
      /**  GainSegVal8  */  
   GainSegVal8:string,
      /**  GainSegVal9  */  
   GainSegVal9:string,
      /**  GainSegVal10  */  
   GainSegVal10:string,
      /**  GainSegVal11  */  
   GainSegVal11:string,
      /**  GainSegVal12  */  
   GainSegVal12:string,
      /**  GainSegVal13  */  
   GainSegVal13:string,
      /**  GainSegVal14  */  
   GainSegVal14:string,
      /**  GainSegVal15  */  
   GainSegVal15:string,
      /**  GainSegVal16  */  
   GainSegVal16:string,
      /**  GainSegVal17  */  
   GainSegVal17:string,
      /**  GainSegVal18  */  
   GainSegVal18:string,
      /**  GainSegVal19  */  
   GainSegVal19:string,
      /**  GainSegVal20  */  
   GainSegVal20:string,
      /**  LossSegVal1  */  
   LossSegVal1:string,
      /**  LossSegVal2  */  
   LossSegVal2:string,
      /**  LossSegVal3  */  
   LossSegVal3:string,
      /**  LossSegVal4  */  
   LossSegVal4:string,
      /**  LossSegVal5  */  
   LossSegVal5:string,
      /**  LossSegVal6  */  
   LossSegVal6:string,
      /**  LossSegVal7  */  
   LossSegVal7:string,
      /**  LossSegVal8  */  
   LossSegVal8:string,
      /**  LossSegVal9  */  
   LossSegVal9:string,
      /**  LossSegVal10  */  
   LossSegVal10:string,
      /**  LossSegVal11  */  
   LossSegVal11:string,
      /**  LossSegVal12  */  
   LossSegVal12:string,
      /**  LossSegVal13  */  
   LossSegVal13:string,
      /**  LossSegVal14  */  
   LossSegVal14:string,
      /**  LossSegVal15  */  
   LossSegVal15:string,
      /**  LossSegVal16  */  
   LossSegVal16:string,
      /**  LossSegVal17  */  
   LossSegVal17:string,
      /**  LossSegVal18  */  
   LossSegVal18:string,
      /**  LossSegVal19  */  
   LossSegVal19:string,
      /**  LossSegVal20  */  
   LossSegVal20:string,
      /**  AccrualSegVal1  */  
   AccrualSegVal1:string,
      /**  AccrualSegVal2  */  
   AccrualSegVal2:string,
      /**  AccrualSegVal3  */  
   AccrualSegVal3:string,
      /**  AccrualSegVal4  */  
   AccrualSegVal4:string,
      /**  AccrualSegVal5  */  
   AccrualSegVal5:string,
      /**  AccrualSegVal6  */  
   AccrualSegVal6:string,
      /**  AccrualSegVal7  */  
   AccrualSegVal7:string,
      /**  AccrualSegVal8  */  
   AccrualSegVal8:string,
      /**  AccrualSegVal9  */  
   AccrualSegVal9:string,
      /**  AccrualSegVal10  */  
   AccrualSegVal10:string,
      /**  AccrualSegVal11  */  
   AccrualSegVal11:string,
      /**  AccrualSegVal12  */  
   AccrualSegVal12:string,
      /**  AccrualSegVal13  */  
   AccrualSegVal13:string,
      /**  AccrualSegVal14  */  
   AccrualSegVal14:string,
      /**  AccrualSegVal15  */  
   AccrualSegVal15:string,
      /**  AccrualSegVal16  */  
   AccrualSegVal16:string,
      /**  AccrualSegVal17  */  
   AccrualSegVal17:string,
      /**  AccrualSegVal18  */  
   AccrualSegVal18:string,
      /**  AccrualSegVal19  */  
   AccrualSegVal19:string,
      /**  AccrualSegVal20  */  
   AccrualSegVal20:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Accrual GL Account description  */  
   AccrualGLDesc:string,
      /**  Gain GL Account Description  */  
   GainGLDesc:string,
      /**  Loss GL Account Description  */  
   LossGLDesc:string,
   BitFlag:number,
   CurrencyCurrencyID:string,
   CurrencyCurrDesc:string,
   CurrencyDocumentDesc:string,
   CurrencyCurrName:string,
   CurrencyCurrSymbol:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_COASegOptRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  System generated number from 1 through 20.  */  
   SegmentNbr:number,
      /**  Segment value used to construct the GL Account.  */  
   SegmentCode:string,
      /**  System generated sequence number  */  
   SubSegmentNbr:number,
      /**   Indicates if a segment is used for the natural account.  Valid values are:
M - Mandatory
O - Optional
N - Not Used  */  
   ValOption:string,
      /**  Indicates the default segment value to be used for this natural account.  */  
   DefaultSegment:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   COASegmentSegmentName:string,
   COASubSegmentSegmentName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_COASegResRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  System generated number from 1 through 20.  */  
   SegmentNbr:number,
      /**  Segment value used to construct the GL Account.  */  
   SegmentCode:string,
      /**  Application DLL name  */  
   RestrictID:string,
      /**  Application name text.  */  
   RestrictText:string,
      /**  Indicates if GL Account entry is prohibited  */  
   FctBlocked:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_COASegValuesListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  System generated number from 1 through 20.  */  
   SegmentNbr:number,
      /**  Segment value used to construct the GL Account.  */  
   SegmentCode:string,
      /**  Name of Segment Value  */  
   SegmentName:string,
      /**  Segment description.  */  
   SegmentDesc:string,
      /**  Short name of the segment value.  */  
   SegmentAbbrev:string,
      /**  Indicates if the segment is active.  Transactions cannot be posted to inactive segments.  */  
   ActiveFlag:boolean,
      /**  Date the segment begins to be used.  It must be less than or equal to the EffectiveTo date.  */  
   EffectiveFrom:string,
      /**  Date the segment is no longer used.  It must be greater than or equal to the EffectiveFrom date, if a value was entered in that field.  */  
   EffectiveTo:string,
      /**  Required for the Natrual Account (segment number 1). Identifies the account category that is used to determine other characteristics.  */  
   Category:string,
      /**  Indicates if the account is a debit or credit and is only valid for the natural account (segment 1).  Valid values are D for Debit and C for Credit.  */  
   NormalBalance:string,
      /**  Rate type used for debit balances.  */  
   DebitRateType:string,
      /**  Rate type used for credit balances  */  
   CreditRateType:string,
      /**  Curency Account  */  
   CurrAcct:boolean,
      /**  Reference Entity type assigned to this COASegValue.  Only valid when the COASegment.RefEntity = "GLCOARefType".  */  
   RefEntityType:string,
      /**   0)      Summarize (default)
1)      Summarize debit and credits separately
2)      No summarization  */  
   Summarization:number,
      /**  This flag determines if journal detail records with this natural account are allowed to be matched.  */  
   MatchingEnabled:boolean,
      /**   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  */  
   Statistical:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Identifies the account category this is used to determine characteristics when the segment value is reversed.  */  
   ReverseCategory:string,
      /**  CurrencyAcctType  */  
   CurrencyAcctType:string,
      /**  RevalueOpt  */  
   RevalueOpt:number,
      /**  COSegDtlNbr  */  
   COSegDtlNbr:number,
      /**  COPrintBalanceInvDtl  */  
   COPrintBalanceInvDtl:boolean,
      /**  Logical indicating if this chart has been used.  */  
   ChartInUse:boolean,
      /**  Logical indicating if this segment value has been used.  */  
   SegValInUse:boolean,
      /**  Logical indicating whether or not the COA has a segment defined as 'entry control' equal to natural account and controls whether or not a segment option record can be entered for a natural account value.  */  
   SegWithSegOneControl:boolean,
      /**  Logical indicating if the reference type is required for this segment value  */  
   RefTypeRqd:boolean,
      /**  Segment number name from the COASegment table.  Used for display purposes in segment value searches where more than one segment number is searched at a time.  */  
   SegNbrName:string,
   ReverseCategoryDescription:string,
      /**  Text describing this category  */  
   CategoryIDDescription:string,
      /**  Description  */  
   CreditRateGrpDescription:string,
      /**  Description  */  
   DebitRateGrpDescription:string,
      /**  Description of the Reference type  */  
   GLCOARefTypeRefTypeDesc:string,
   StatisticalDesc:string,
   EffectiveRevalueOpt:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_COASegValuesListTableset{
   COASegValuesList:Erp_Tablesets_COASegValuesListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_COASegValuesRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  System generated number from 1 through 20.  */  
   SegmentNbr:number,
      /**  Segment value used to construct the GL Account.  */  
   SegmentCode:string,
      /**  Name of Segment Value  */  
   SegmentName:string,
      /**  Segment description.  */  
   SegmentDesc:string,
      /**  Short name of the segment value.  */  
   SegmentAbbrev:string,
      /**  Indicates if the segment is active.  Transactions cannot be posted to inactive segments.  */  
   ActiveFlag:boolean,
      /**  Date the segment begins to be used.  It must be less than or equal to the EffectiveTo date.  */  
   EffectiveFrom:string,
      /**  Date the segment is no longer used.  It must be greater than or equal to the EffectiveFrom date, if a value was entered in that field.  */  
   EffectiveTo:string,
      /**  Required for the Natrual Account (segment number 1). Identifies the account category that is used to determine other characteristics.  */  
   Category:string,
      /**  Indicates if the account is a debit or credit and is only valid for the natural account (segment 1).  Valid values are D for Debit and C for Credit.  */  
   NormalBalance:string,
      /**  Rate type used for debit balances.  */  
   DebitRateType:string,
      /**  Rate type used for credit balances  */  
   CreditRateType:string,
      /**  Curency Account  */  
   CurrAcct:boolean,
      /**  Reference Entity type assigned to this COASegValue.  Only valid when the COASegment.RefEntity = "GLCOARefType".  */  
   RefEntityType:string,
      /**   0)      Summarize (default)
1)      Summarize debit and credits separately
2)      No summarization  */  
   Summarization:number,
      /**  This flag determines if journal detail records with this natural account are allowed to be matched.  */  
   MatchingEnabled:boolean,
      /**   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  */  
   Statistical:number,
      /**  StatUOMCode  */  
   StatUOMCode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Identifies the account category this is used to determine characteristics when the segment value is reversed.  */  
   ReverseCategory:string,
      /**  External financial analysis code linked to the natural account.  */  
   ExtAnalysisCode:string,
      /**  CurrencyAcctType  */  
   CurrencyAcctType:string,
      /**  RevalueOpt  */  
   RevalueOpt:number,
      /**  GLGainAcctContext  */  
   GLGainAcctContext:string,
      /**  GLLossAcctContext  */  
   GLLossAcctContext:string,
      /**  GainAccount  */  
   GainAccount:string,
      /**  LossAccount  */  
   LossAccount:string,
      /**  AccrualAccount  */  
   AccrualAccount:string,
      /**  GainSegVal1  */  
   GainSegVal1:string,
      /**  GainSegVal2  */  
   GainSegVal2:string,
      /**  GainSegVal3  */  
   GainSegVal3:string,
      /**  GainSegVal4  */  
   GainSegVal4:string,
      /**  GainSegVal5  */  
   GainSegVal5:string,
      /**  GainSegVal6  */  
   GainSegVal6:string,
      /**  GainSegVal7  */  
   GainSegVal7:string,
      /**  GainSegVal8  */  
   GainSegVal8:string,
      /**  GainSegVal9  */  
   GainSegVal9:string,
      /**  GainSegVal10  */  
   GainSegVal10:string,
      /**  GainSegVal11  */  
   GainSegVal11:string,
      /**  GainSegVal12  */  
   GainSegVal12:string,
      /**  GainSegVal13  */  
   GainSegVal13:string,
      /**  GainSegVal14  */  
   GainSegVal14:string,
      /**  GainSegVal15  */  
   GainSegVal15:string,
      /**  GainSegVal16  */  
   GainSegVal16:string,
      /**  GainSegVal17  */  
   GainSegVal17:string,
      /**  GainSegVal18  */  
   GainSegVal18:string,
      /**  GainSegVal19  */  
   GainSegVal19:string,
      /**  GainSegVal20  */  
   GainSegVal20:string,
      /**  LossSegVal1  */  
   LossSegVal1:string,
      /**  LossSegVal2  */  
   LossSegVal2:string,
      /**  LossSegVal3  */  
   LossSegVal3:string,
      /**  LossSegVal4  */  
   LossSegVal4:string,
      /**  LossSegVal5  */  
   LossSegVal5:string,
      /**  LossSegVal6  */  
   LossSegVal6:string,
      /**  LossSegVal7  */  
   LossSegVal7:string,
      /**  LossSegVal8  */  
   LossSegVal8:string,
      /**  LossSegVal9  */  
   LossSegVal9:string,
      /**  LossSegVal10  */  
   LossSegVal10:string,
      /**  LossSegVal11  */  
   LossSegVal11:string,
      /**  LossSegVal12  */  
   LossSegVal12:string,
      /**  LossSegVal13  */  
   LossSegVal13:string,
      /**  LossSegVal14  */  
   LossSegVal14:string,
      /**  LossSegVal15  */  
   LossSegVal15:string,
      /**  LossSegVal16  */  
   LossSegVal16:string,
      /**  LossSegVal17  */  
   LossSegVal17:string,
      /**  LossSegVal18  */  
   LossSegVal18:string,
      /**  LossSegVal19  */  
   LossSegVal19:string,
      /**  LossSegVal20  */  
   LossSegVal20:string,
      /**  AccrualSegVal1  */  
   AccrualSegVal1:string,
      /**  AccrualSegVal2  */  
   AccrualSegVal2:string,
      /**  AccrualSegVal3  */  
   AccrualSegVal3:string,
      /**  AccrualSegVal4  */  
   AccrualSegVal4:string,
      /**  AccrualSegVal5  */  
   AccrualSegVal5:string,
      /**  AccrualSegVal6  */  
   AccrualSegVal6:string,
      /**  AccrualSegVal7  */  
   AccrualSegVal7:string,
      /**  AccrualSegVal8  */  
   AccrualSegVal8:string,
      /**  AccrualSegVal9  */  
   AccrualSegVal9:string,
      /**  AccrualSegVal10  */  
   AccrualSegVal10:string,
      /**  AccrualSegVal11  */  
   AccrualSegVal11:string,
      /**  AccrualSegVal12  */  
   AccrualSegVal12:string,
      /**  AccrualSegVal13  */  
   AccrualSegVal13:string,
      /**  AccrualSegVal14  */  
   AccrualSegVal14:string,
      /**  AccrualSegVal15  */  
   AccrualSegVal15:string,
      /**  AccrualSegVal16  */  
   AccrualSegVal16:string,
      /**  AccrualSegVal17  */  
   AccrualSegVal17:string,
      /**  AccrualSegVal18  */  
   AccrualSegVal18:string,
      /**  AccrualSegVal19  */  
   AccrualSegVal19:string,
      /**  AccrualSegVal20  */  
   AccrualSegVal20:string,
      /**  COSegDtlNbr  */  
   COSegDtlNbr:number,
      /**  COPrintBalanceInvDtl  */  
   COPrintBalanceInvDtl:boolean,
      /**  Non-Admissible Expense Code (CSF Belgium)  */  
   BENAEID:string,
      /**  Mapped  */  
   Mapped:boolean,
      /**  One of the UD codes having a CodeTypeID equal to GLRepCat. Or, if GLRepCat does not exist, then it may be free text.  */  
   ReportCategory:string,
      /**  ReverseReportCategory  */  
   ReverseReportCategory:string,
      /**  LinkedPlant  */  
   LinkedPlant:string,
      /**  Accrual Account Description  */  
   AccrualAcctDesc:string,
      /**  Gain Account Description  */  
   GainAcctDesc:string,
   GlbValuesFlag:boolean,
   GlobalSegValues:boolean,
   GlobalSegValuesLock:boolean,
      /**  Loss Account Description  */  
   LossAcctDesc:string,
      /**  Internal logical used by UI that indicates if GLAccounts exist for this COA and that the display gl account must be rebuilt  */  
   RebuildGLAccts:boolean,
      /**  Logical indicating if the reference type is required for this segment value  */  
   RefTypeRqd:boolean,
   ReverseCategoryDescription:string,
      /**  Segment number name from the COASegment table.  Used for display purposes in segment value searches where more than one segment number is searched at a time.  */  
   SegNbrName:string,
      /**  Logical indicating if this segment value has been used.  */  
   SegValInUse:boolean,
      /**  Logical indicating whether or not the COA has a segment defined as 'entry control' equal to natural account and controls whether or not a segment option record can be entered for a natural account value.  */  
   SegWithSegOneControl:boolean,
   StatisticalDesc:string,
      /**  Logical indicating if this chart has been used.  */  
   ChartInUse:boolean,
   BitFlag:number,
   CategoryIDDescription:string,
   COASegmentSiteSegment:boolean,
   COASegmentSegmentName:string,
   COSegDtlSegmentName:string,
   CreditRateGrpDescription:string,
   DebitRateGrpDescription:string,
   GLCOARefTypeRefTypeDesc:string,
      /**  RowMod  */  
   RowMod:string,
   UD_SysRevID:string,
   BudgetSegCode_c:string,
   BudgetReportGroup_c:string,
}

export interface Erp_Tablesets_COASegValuesTableset{
   COASegValues:Erp_Tablesets_COASegValuesRow[],
   COASegAcct:Erp_Tablesets_COASegAcctRow[],
   COASegOpt:Erp_Tablesets_COASegOptRow[],
   COASegRes:Erp_Tablesets_COASegResRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_InterSiteAccountPairRow{
   Company:string,
   BookID:string,
   SourcePlant:string,
   DueFromSegValue1:string,
   DueFromSegValue2:string,
   DueFromSegValue3:string,
   DueFromSegValue4:string,
   DueFromSegValue5:string,
   DueFromSegValue6:string,
   DueFromSegValue7:string,
   DueFromSegValue8:string,
   DueFromSegValue9:string,
   DueFromSegValue10:string,
   DueFromSegValue11:string,
   DueFromSegValue12:string,
   DueFromSegValue13:string,
   DueFromSegValue14:string,
   DueFromSegValue15:string,
   DueFromSegValue16:string,
   DueFromSegValue17:string,
   DueFromSegValue18:string,
   DueFromSegValue19:string,
   DueFromSegValue20:string,
   TargetPlant:string,
   DueToSegValue1:string,
   DueToSegValue2:string,
   DueToSegValue3:string,
   DueToSegValue4:string,
   DueToSegValue5:string,
   DueToSegValue6:string,
   DueToSegValue7:string,
   DueToSegValue8:string,
   DueToSegValue9:string,
   DueToSegValue10:string,
   DueToSegValue11:string,
   DueToSegValue12:string,
   DueToSegValue13:string,
   DueToSegValue14:string,
   DueToSegValue15:string,
   DueToSegValue16:string,
   DueToSegValue17:string,
   DueToSegValue18:string,
   DueToSegValue19:string,
   DueToSegValue20:string,
   COACode:string,
   BookDescription:string,
   SourcePlantName:string,
   TargetPlantName:string,
      /**  Indicates if the due from account is invalid  */  
   InvalidDueFromAccount:boolean,
   DueFromGLAccount:string,
   DueFromGLAccountDesc:string,
   DueToGLAccount:string,
      /**  Indicates if the due to account is invalid  */  
   InvalidDueToAccount:boolean,
   DueToGLAccountDesc:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SiteSegmentSetupRow{
      /**  Chart of Account ID  */  
   COACode:string,
      /**  GL Control Identifier.  */  
   GLControlCode:string,
      /**  Linked Site  */  
   LinkedPlant:string,
      /**  Short name of the segment value.  */  
   SegmentAbbrev:string,
   SegmentCode:string,
      /**  Name of Segment Value  */  
   SegmentName:string,
      /**  Segment Description  */  
   SegmentDesc:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SiteSegmentSetupTableset{
   InterSiteAccountPair:Erp_Tablesets_InterSiteAccountPairRow[],
   SiteSegmentSetup:Erp_Tablesets_SiteSegmentSetupRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtCOASegValuesTableset{
   COASegValues:Erp_Tablesets_COASegValuesRow[],
   COASegAcct:Erp_Tablesets_COASegAcctRow[],
   COASegOpt:Erp_Tablesets_COASegOptRow[],
   COASegRes:Erp_Tablesets_COASegResRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ds
   */  
export interface GenerateSiteSegmentSetupData_input{
   ds:Erp_Tablesets_SiteSegmentSetupTableset[],
}

export interface GenerateSiteSegmentSetupData_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SiteSegmentSetupTableset[],
}
}

   /** Required : 
      @param coACode
      @param segmentNbr
      @param segmentCode
   */  
export interface GetByID_input{
   coACode:string,
   segmentNbr:number,
   segmentCode:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_COASegValuesTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_COASegValuesTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_COASegValuesTableset[],
}

   /** Required : 
      @param COACode
      @param SegmentNbr
      @param GlobalLock
   */  
export interface GetCOASegmentGlobalFields_input{
   COACode:string,
   SegmentNbr:number,
   GlobalLock:boolean,
}

export interface GetCOASegmentGlobalFields_output{
   returnObj:string,
}

   /** Required : 
      @param coaCode
      @param ds
   */  
export interface GetInterSiteAccountPairs_input{
      /**  COA Code  */  
   coaCode:string,
   ds:Erp_Tablesets_SiteSegmentSetupTableset[],
}

export interface GetInterSiteAccountPairs_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SiteSegmentSetupTableset[],
}
}

   /** Required : 
      @param WhereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetListCBOnly_input{
   WhereClause:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetListCBOnly_output{
   returnObj:Erp_Tablesets_COASegValuesListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
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
   returnObj:Erp_Tablesets_COASegValuesListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param coACode
      @param segmentNbr
      @param segmentCode
   */  
export interface GetNewCOASegAcct_input{
   ds:Erp_Tablesets_COASegValuesTableset[],
   coACode:string,
   segmentNbr:number,
   segmentCode:string,
}

export interface GetNewCOASegAcct_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_COASegValuesTableset[],
}
}

   /** Required : 
      @param ds
      @param coACode
      @param segmentNbr
      @param segmentCode
   */  
export interface GetNewCOASegOpt_input{
   ds:Erp_Tablesets_COASegValuesTableset[],
   coACode:string,
   segmentNbr:number,
   segmentCode:string,
}

export interface GetNewCOASegOpt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_COASegValuesTableset[],
}
}

   /** Required : 
      @param ds
      @param coACode
      @param segmentNbr
      @param segmentCode
   */  
export interface GetNewCOASegRes_input{
   ds:Erp_Tablesets_COASegValuesTableset[],
   coACode:string,
   segmentNbr:number,
   segmentCode:string,
}

export interface GetNewCOASegRes_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_COASegValuesTableset[],
}
}

   /** Required : 
      @param ds
      @param coACode
      @param segmentNbr
   */  
export interface GetNewCOASegValues_input{
   ds:Erp_Tablesets_COASegValuesTableset[],
   coACode:string,
   segmentNbr:number,
}

export interface GetNewCOASegValues_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_COASegValuesTableset[],
}
}

   /** Required : 
      @param whereClauseCOASegValues
      @param whereClauseCOASegAcct
      @param whereClauseCOASegOpt
      @param whereClauseCOASegRes
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseCOASegValues:string,
   whereClauseCOASegAcct:string,
   whereClauseCOASegOpt:string,
   whereClauseCOASegRes:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_COASegValuesTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param coaCode
      @param ds
   */  
export interface GetSiteSegmentSetupData_input{
   coaCode:string,
   ds:Erp_Tablesets_SiteSegmentSetupTableset[],
}

export interface GetSiteSegmentSetupData_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SiteSegmentSetupTableset[],
}
}

   /** Required : 
      @param COACode
   */  
export interface GetSiteSetting_input{
   COACode:string,
}

export interface GetSiteSetting_output{
parameters : {
      /**  output parameters  */  
   showSiteWizard:boolean,
}
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
      @param ds
   */  
export interface IntersiteAccountPairsApply_input{
   ds:Erp_Tablesets_SiteSegmentSetupTableset[],
}

export interface IntersiteAccountPairsApply_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SiteSegmentSetupTableset[],
   invalidAccountMessage:string,
   incompletePairMessage:string,
}
}

   /** Required : 
      @param ipCompany
      @param ipCOACode
      @param ipSegmentCode
   */  
export interface IsStatOnlySegment_input{
   ipCompany:string,
   ipCOACode:string,
   ipSegmentCode:string,
}

export interface IsStatOnlySegment_output{
   returnObj:boolean,
}

   /** Required : 
      @param linkedPlant
      @param segmentCode
      @param ds
   */  
export interface RemoveSiteSegmentCodeDuplicate_input{
   linkedPlant:string,
   segmentCode:string,
   ds:Erp_Tablesets_SiteSegmentSetupTableset[],
}

export interface RemoveSiteSegmentCodeDuplicate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SiteSegmentSetupTableset[],
}
}

   /** Required : 
      @param plant
      @param ds
   */  
export interface SiteSegmentChanged_input{
   plant:string,
   ds:Erp_Tablesets_SiteSegmentSetupTableset[],
}

export interface SiteSegmentChanged_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SiteSegmentSetupTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface SiteSegmentSetupApply_input{
   ds:Erp_Tablesets_SiteSegmentSetupTableset[],
}

export interface SiteSegmentSetupApply_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SiteSegmentSetupTableset[],
   msg:string,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtCOASegValuesTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtCOASegValuesTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_COASegValuesTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_COASegValuesTableset[],
}
}

   /** Required : 
      @param coaCode
      @param segNbr
   */  
export interface ValidateCOACodeSite_input{
      /**  COA code entered  */  
   coaCode:string,
      /**  segNbr  */  
   segNbr:string,
}

export interface ValidateCOACodeSite_output{
parameters : {
      /**  output parameters  */  
   opDescription:string,
   opSegmentNbr:number,
   opSegmentName:string,
   opGlobalCOA:boolean,
   opGlobalSegment:boolean,
   opSiteSegment:boolean,
}
}

   /** Required : 
      @param coaCode
      @param segNbr
   */  
export interface ValidateCOACode_input{
      /**  COA code entered  */  
   coaCode:string,
      /**  segNbr  */  
   segNbr:string,
}

export interface ValidateCOACode_output{
parameters : {
      /**  output parameters  */  
   opDescription:string,
   opSegmentNbr:number,
   opSegmentName:string,
   opGlobalCOA:boolean,
   opGlobalSegment:boolean,
}
}

   /** Required : 
      @param ipCOACode
      @param ipSegmentNbr
   */  
export interface ValidateCOASegment_input{
      /**  COA Code  */  
   ipCOACode:string,
      /**  Segment Number  */  
   ipSegmentNbr:number,
}

export interface ValidateCOASegment_output{
}

   /** Required : 
      @param ipCOACode
      @param ipSegmentCode
      @param ipCurrencyAcct
      @param CurrencyAcctType
   */  
export interface ValidateCurrencyAccount_input{
   ipCOACode:string,
   ipSegmentCode:string,
   ipCurrencyAcct:boolean,
   CurrencyAcctType:string,
}

export interface ValidateCurrencyAccount_output{
}

   /** Required : 
      @param ipCOACode
      @param ipSubSegmentNbr
      @param ipSegmentCode
   */  
export interface ValidateDefaultSegment_input{
   ipCOACode:string,
   ipSubSegmentNbr:number,
   ipSegmentCode:string,
}

export interface ValidateDefaultSegment_output{
}

   /** Required : 
      @param pbookID
      @param pCOACode
   */  
export interface getBookRevOpt_input{
   pbookID:string,
   pCOACode:string,
}

export interface getBookRevOpt_output{
parameters : {
      /**  output parameters  */  
   pEffRevOpt:number,
}
}

