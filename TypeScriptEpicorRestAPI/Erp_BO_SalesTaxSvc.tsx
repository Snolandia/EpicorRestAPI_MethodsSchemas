import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.SalesTaxSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/$metadata", {
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
   Description: Get SalesTaxes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SalesTaxes
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SalesTaxRow
   */  
export function get_SalesTaxes(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SalesTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/SalesTaxes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SalesTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SalesTaxes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SalesTaxRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SalesTaxRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SalesTaxes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/SalesTaxes", {
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
   Summary: Calls GetByID to retrieve the SalesTax item
   Description: Calls GetByID to retrieve the SalesTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SalesTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SalesTaxRow
   */  
export function get_SalesTaxes_Company_TaxCode(Company:string, TaxCode:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_SalesTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/SalesTaxes(" + Company + "," + TaxCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_SalesTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update SalesTax for the service
   Description: Calls UpdateExt to update SalesTax. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SalesTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SalesTaxRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_SalesTaxes_Company_TaxCode(Company:string, TaxCode:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/SalesTaxes(" + Company + "," + TaxCode + ")", {
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
   Summary: Call UpdateExt to delete SalesTax item
   Description: Call UpdateExt to delete SalesTax item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SalesTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_SalesTaxes_Company_TaxCode(Company:string, TaxCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/SalesTaxes(" + Company + "," + TaxCode + ")", {
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
   Description: Get LangDescs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_LangDescs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LangDescRow
   */  
export function get_SalesTaxes_Company_TaxCode_LangDescs(Company:string, TaxCode:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LangDescRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/SalesTaxes(" + Company + "," + TaxCode + ")/LangDescs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LangDescRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the LangDesc item
   Description: Calls GetByID to retrieve the LangDesc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LangDesc1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param TableName Desc: TableName   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param LangNameID Desc: LangNameID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LangDescRow
   */  
export function get_SalesTaxes_Company_TaxCode_LangDescs_Company_TableName_Key1_Key2_Key3_LangNameID(Company:string, TaxCode:string, TableName:string, Key1:string, Key2:string, Key3:string, LangNameID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LangDescRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/SalesTaxes(" + Company + "," + TaxCode + ")/LangDescs(" + Company + "," + TableName + "," + Key1 + "," + Key2 + "," + Key3 + "," + LangNameID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_LangDescRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get SalesTRCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_SalesTRCs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SalesTRCRow
   */  
export function get_SalesTaxes_Company_TaxCode_SalesTRCs(Company:string, TaxCode:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SalesTRCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/SalesTaxes(" + Company + "," + TaxCode + ")/SalesTRCs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SalesTRCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the SalesTRC item
   Description: Calls GetByID to retrieve the SalesTRC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SalesTRC1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SalesTRCRow
   */  
export function get_SalesTaxes_Company_TaxCode_SalesTRCs_Company_TaxCode_RateCode(Company:string, TaxCode:string, RateCode:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_SalesTRCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/SalesTaxes(" + Company + "," + TaxCode + ")/SalesTRCs(" + Company + "," + TaxCode + "," + RateCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_SalesTRCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get LangDescs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LangDescs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LangDescRow
   */  
export function get_LangDescs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LangDescRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/LangDescs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LangDescRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LangDescs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LangDescRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LangDescRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LangDescs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/LangDescs", {
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
   Summary: Calls GetByID to retrieve the LangDesc item
   Description: Calls GetByID to retrieve the LangDesc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LangDesc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TableName Desc: TableName   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param LangNameID Desc: LangNameID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LangDescRow
   */  
export function get_LangDescs_Company_TableName_Key1_Key2_Key3_LangNameID(Company:string, TableName:string, Key1:string, Key2:string, Key3:string, LangNameID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LangDescRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/LangDescs(" + Company + "," + TableName + "," + Key1 + "," + Key2 + "," + Key3 + "," + LangNameID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_LangDescRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update LangDesc for the service
   Description: Calls UpdateExt to update LangDesc. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LangDesc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TableName Desc: TableName   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param LangNameID Desc: LangNameID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LangDescRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_LangDescs_Company_TableName_Key1_Key2_Key3_LangNameID(Company:string, TableName:string, Key1:string, Key2:string, Key3:string, LangNameID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/LangDescs(" + Company + "," + TableName + "," + Key1 + "," + Key2 + "," + Key3 + "," + LangNameID + ")", {
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
   Summary: Call UpdateExt to delete LangDesc item
   Description: Call UpdateExt to delete LangDesc item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LangDesc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TableName Desc: TableName   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param LangNameID Desc: LangNameID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_LangDescs_Company_TableName_Key1_Key2_Key3_LangNameID(Company:string, TableName:string, Key1:string, Key2:string, Key3:string, LangNameID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/LangDescs(" + Company + "," + TableName + "," + Key1 + "," + Key2 + "," + Key3 + "," + LangNameID + ")", {
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
   Description: Get SalesTRCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SalesTRCs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SalesTRCRow
   */  
export function get_SalesTRCs(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SalesTRCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/SalesTRCs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SalesTRCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SalesTRCs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SalesTRCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SalesTRCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SalesTRCs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/SalesTRCs", {
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
   Summary: Calls GetByID to retrieve the SalesTRC item
   Description: Calls GetByID to retrieve the SalesTRC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SalesTRC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SalesTRCRow
   */  
export function get_SalesTRCs_Company_TaxCode_RateCode(Company:string, TaxCode:string, RateCode:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_SalesTRCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/SalesTRCs(" + Company + "," + TaxCode + "," + RateCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_SalesTRCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update SalesTRC for the service
   Description: Calls UpdateExt to update SalesTRC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SalesTRC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SalesTRCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_SalesTRCs_Company_TaxCode_RateCode(Company:string, TaxCode:string, RateCode:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/SalesTRCs(" + Company + "," + TaxCode + "," + RateCode + ")", {
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
   Summary: Call UpdateExt to delete SalesTRC item
   Description: Call UpdateExt to delete SalesTRC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SalesTRC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_SalesTRCs_Company_TaxCode_RateCode(Company:string, TaxCode:string, RateCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/SalesTRCs(" + Company + "," + TaxCode + "," + RateCode + ")", {
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
   Description: Get EntityGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_EntityGLCs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EntityGLCRow
   */  
export function get_SalesTRCs_Company_TaxCode_RateCode_EntityGLCs(Company:string, TaxCode:string, RateCode:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/SalesTRCs(" + Company + "," + TaxCode + "," + RateCode + ")/EntityGLCs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EntityGLC item
   Description: Calls GetByID to retrieve the EntityGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EntityGLC1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param Key6 Desc: Key6   Required: True   Allow empty value : True
      @param GLControlType Desc: GLControlType   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   */  
export function get_SalesTRCs_Company_TaxCode_RateCode_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company:string, TaxCode:string, RateCode:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, GLControlType:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_EntityGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/SalesTRCs(" + Company + "," + TaxCode + "," + RateCode + ")/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_EntityGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get SalesTxcs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_SalesTxcs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SalesTxcRow
   */  
export function get_SalesTRCs_Company_TaxCode_RateCode_SalesTxcs(Company:string, TaxCode:string, RateCode:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SalesTxcRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/SalesTRCs(" + Company + "," + TaxCode + "," + RateCode + ")/SalesTxcs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SalesTxcRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the SalesTxc item
   Description: Calls GetByID to retrieve the SalesTxc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SalesTxc1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param TaxCatID Desc: TaxCatID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SalesTxcRow
   */  
export function get_SalesTRCs_Company_TaxCode_RateCode_SalesTxcs_Company_TaxCode_RateCode_TaxCatID(Company:string, TaxCode:string, RateCode:string, TaxCatID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_SalesTxcRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/SalesTRCs(" + Company + "," + TaxCode + "," + RateCode + ")/SalesTxcs(" + Company + "," + TaxCode + "," + RateCode + "," + TaxCatID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_SalesTxcRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get TaxBoxes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TaxBoxes1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxBoxRow
   */  
export function get_SalesTRCs_Company_TaxCode_RateCode_TaxBoxes(Company:string, TaxCode:string, RateCode:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxBoxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/SalesTRCs(" + Company + "," + TaxCode + "," + RateCode + ")/TaxBoxes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxBoxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the TaxBox item
   Description: Calls GetByID to retrieve the TaxBox item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxBox1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param BoxCode Desc: BoxCode   Required: True   Allow empty value : True
      @param SourceModule Desc: SourceModule   Required: True   Allow empty value : True
      @param AmountType Desc: AmountType   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxBoxRow
   */  
export function get_SalesTRCs_Company_TaxCode_RateCode_TaxBoxes_Company_TaxCode_RateCode_BoxCode_SourceModule_AmountType_ECAcquisitionSeq(Company:string, TaxCode:string, RateCode:string, BoxCode:string, SourceModule:string, AmountType:string, ECAcquisitionSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TaxBoxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/SalesTRCs(" + Company + "," + TaxCode + "," + RateCode + ")/TaxBoxes(" + Company + "," + TaxCode + "," + RateCode + "," + BoxCode + "," + SourceModule + "," + AmountType + "," + ECAcquisitionSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_TaxBoxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get TaxRates items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TaxRates1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxRateRow
   */  
export function get_SalesTRCs_Company_TaxCode_RateCode_TaxRates(Company:string, TaxCode:string, RateCode:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxRateRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/SalesTRCs(" + Company + "," + TaxCode + "," + RateCode + ")/TaxRates", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxRateRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the TaxRate item
   Description: Calls GetByID to retrieve the TaxRate item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxRate1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param EffectiveFrom Desc: EffectiveFrom   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxRateRow
   */  
export function get_SalesTRCs_Company_TaxCode_RateCode_TaxRates_Company_TaxCode_RateCode_EffectiveFrom(Company:string, TaxCode:string, RateCode:string, EffectiveFrom:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TaxRateRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/SalesTRCs(" + Company + "," + TaxCode + "," + RateCode + ")/TaxRates(" + Company + "," + TaxCode + "," + RateCode + "," + EffectiveFrom + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_TaxRateRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get PLSAFTCodes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PLSAFTCodes1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PLSAFTCodeRow
   */  
export function get_SalesTRCs_Company_TaxCode_RateCode_PLSAFTCodes(Company:string, TaxCode:string, RateCode:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PLSAFTCodeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/SalesTRCs(" + Company + "," + TaxCode + "," + RateCode + ")/PLSAFTCodes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PLSAFTCodeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PLSAFTCode item
   Description: Calls GetByID to retrieve the PLSAFTCode item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PLSAFTCode1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param SAFTCode Desc: SAFTCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PLSAFTCodeRow
   */  
export function get_SalesTRCs_Company_TaxCode_RateCode_PLSAFTCodes_Company_RateCode_TaxCode_SAFTCode(Company:string, TaxCode:string, RateCode:string, SAFTCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PLSAFTCodeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/SalesTRCs(" + Company + "," + TaxCode + "," + RateCode + ")/PLSAFTCodes(" + Company + "," + RateCode + "," + TaxCode + "," + SAFTCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PLSAFTCodeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get EntityGLCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EntityGLCs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EntityGLCRow
   */  
export function get_EntityGLCs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/EntityGLCs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EntityGLCs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EntityGLCs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/EntityGLCs", {
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
   Summary: Calls GetByID to retrieve the EntityGLC item
   Description: Calls GetByID to retrieve the EntityGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EntityGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param Key6 Desc: Key6   Required: True   Allow empty value : True
      @param GLControlType Desc: GLControlType   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   */  
export function get_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, GLControlType:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_EntityGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_EntityGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update EntityGLC for the service
   Description: Calls UpdateExt to update EntityGLC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EntityGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param Key6 Desc: Key6   Required: True   Allow empty value : True
      @param GLControlType Desc: GLControlType   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, GLControlType:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
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
   Summary: Call UpdateExt to delete EntityGLC item
   Description: Call UpdateExt to delete EntityGLC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EntityGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param Key6 Desc: Key6   Required: True   Allow empty value : True
      @param GLControlType Desc: GLControlType   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, GLControlType:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
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
   Description: Get SalesTxcs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SalesTxcs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SalesTxcRow
   */  
export function get_SalesTxcs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SalesTxcRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/SalesTxcs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SalesTxcRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SalesTxcs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SalesTxcRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SalesTxcRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SalesTxcs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/SalesTxcs", {
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
   Summary: Calls GetByID to retrieve the SalesTxc item
   Description: Calls GetByID to retrieve the SalesTxc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SalesTxc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param TaxCatID Desc: TaxCatID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SalesTxcRow
   */  
export function get_SalesTxcs_Company_TaxCode_RateCode_TaxCatID(Company:string, TaxCode:string, RateCode:string, TaxCatID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_SalesTxcRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/SalesTxcs(" + Company + "," + TaxCode + "," + RateCode + "," + TaxCatID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_SalesTxcRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update SalesTxc for the service
   Description: Calls UpdateExt to update SalesTxc. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SalesTxc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param TaxCatID Desc: TaxCatID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SalesTxcRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_SalesTxcs_Company_TaxCode_RateCode_TaxCatID(Company:string, TaxCode:string, RateCode:string, TaxCatID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/SalesTxcs(" + Company + "," + TaxCode + "," + RateCode + "," + TaxCatID + ")", {
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
   Summary: Call UpdateExt to delete SalesTxc item
   Description: Call UpdateExt to delete SalesTxc item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SalesTxc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param TaxCatID Desc: TaxCatID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_SalesTxcs_Company_TaxCode_RateCode_TaxCatID(Company:string, TaxCode:string, RateCode:string, TaxCatID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/SalesTxcs(" + Company + "," + TaxCode + "," + RateCode + "," + TaxCatID + ")", {
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
   Description: Get TaxBoxes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TaxBoxes
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxBoxRow
   */  
export function get_TaxBoxes(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxBoxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/TaxBoxes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxBoxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TaxBoxes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TaxBoxRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TaxBoxRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TaxBoxes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/TaxBoxes", {
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
   Summary: Calls GetByID to retrieve the TaxBox item
   Description: Calls GetByID to retrieve the TaxBox item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxBox
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param BoxCode Desc: BoxCode   Required: True   Allow empty value : True
      @param SourceModule Desc: SourceModule   Required: True   Allow empty value : True
      @param AmountType Desc: AmountType   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxBoxRow
   */  
export function get_TaxBoxes_Company_TaxCode_RateCode_BoxCode_SourceModule_AmountType_ECAcquisitionSeq(Company:string, TaxCode:string, RateCode:string, BoxCode:string, SourceModule:string, AmountType:string, ECAcquisitionSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TaxBoxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/TaxBoxes(" + Company + "," + TaxCode + "," + RateCode + "," + BoxCode + "," + SourceModule + "," + AmountType + "," + ECAcquisitionSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_TaxBoxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update TaxBox for the service
   Description: Calls UpdateExt to update TaxBox. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TaxBox
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param BoxCode Desc: BoxCode   Required: True   Allow empty value : True
      @param SourceModule Desc: SourceModule   Required: True   Allow empty value : True
      @param AmountType Desc: AmountType   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TaxBoxRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_TaxBoxes_Company_TaxCode_RateCode_BoxCode_SourceModule_AmountType_ECAcquisitionSeq(Company:string, TaxCode:string, RateCode:string, BoxCode:string, SourceModule:string, AmountType:string, ECAcquisitionSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/TaxBoxes(" + Company + "," + TaxCode + "," + RateCode + "," + BoxCode + "," + SourceModule + "," + AmountType + "," + ECAcquisitionSeq + ")", {
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
   Summary: Call UpdateExt to delete TaxBox item
   Description: Call UpdateExt to delete TaxBox item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TaxBox
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param BoxCode Desc: BoxCode   Required: True   Allow empty value : True
      @param SourceModule Desc: SourceModule   Required: True   Allow empty value : True
      @param AmountType Desc: AmountType   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_TaxBoxes_Company_TaxCode_RateCode_BoxCode_SourceModule_AmountType_ECAcquisitionSeq(Company:string, TaxCode:string, RateCode:string, BoxCode:string, SourceModule:string, AmountType:string, ECAcquisitionSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/TaxBoxes(" + Company + "," + TaxCode + "," + RateCode + "," + BoxCode + "," + SourceModule + "," + AmountType + "," + ECAcquisitionSeq + ")", {
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
   Description: Get TaxRates items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TaxRates
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxRateRow
   */  
export function get_TaxRates(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxRateRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/TaxRates", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxRateRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TaxRates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TaxRateRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TaxRateRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TaxRates(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/TaxRates", {
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
   Summary: Calls GetByID to retrieve the TaxRate item
   Description: Calls GetByID to retrieve the TaxRate item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxRate
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param EffectiveFrom Desc: EffectiveFrom   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxRateRow
   */  
export function get_TaxRates_Company_TaxCode_RateCode_EffectiveFrom(Company:string, TaxCode:string, RateCode:string, EffectiveFrom:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TaxRateRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/TaxRates(" + Company + "," + TaxCode + "," + RateCode + "," + EffectiveFrom + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_TaxRateRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update TaxRate for the service
   Description: Calls UpdateExt to update TaxRate. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TaxRate
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param EffectiveFrom Desc: EffectiveFrom   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TaxRateRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_TaxRates_Company_TaxCode_RateCode_EffectiveFrom(Company:string, TaxCode:string, RateCode:string, EffectiveFrom:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/TaxRates(" + Company + "," + TaxCode + "," + RateCode + "," + EffectiveFrom + ")", {
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
   Summary: Call UpdateExt to delete TaxRate item
   Description: Call UpdateExt to delete TaxRate item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TaxRate
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param EffectiveFrom Desc: EffectiveFrom   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_TaxRates_Company_TaxCode_RateCode_EffectiveFrom(Company:string, TaxCode:string, RateCode:string, EffectiveFrom:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/TaxRates(" + Company + "," + TaxCode + "," + RateCode + "," + EffectiveFrom + ")", {
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
   Description: Get EffRateEntityGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_EffRateEntityGLCs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param EffectiveFrom Desc: EffectiveFrom   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EffRateEntityGLCRow
   */  
export function get_TaxRates_Company_TaxCode_RateCode_EffectiveFrom_EffRateEntityGLCs(Company:string, TaxCode:string, RateCode:string, EffectiveFrom:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EffRateEntityGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/TaxRates(" + Company + "," + TaxCode + "," + RateCode + "," + EffectiveFrom + ")/EffRateEntityGLCs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EffRateEntityGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EffRateEntityGLC item
   Description: Calls GetByID to retrieve the EffRateEntityGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EffRateEntityGLC1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param EffectiveFrom Desc: EffectiveFrom   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param Key6 Desc: Key6   Required: True   Allow empty value : True
      @param GLControlType Desc: GLControlType   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EffRateEntityGLCRow
   */  
export function get_TaxRates_Company_TaxCode_RateCode_EffectiveFrom_EffRateEntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company:string, TaxCode:string, RateCode:string, EffectiveFrom:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, GLControlType:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_EffRateEntityGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/TaxRates(" + Company + "," + TaxCode + "," + RateCode + "," + EffectiveFrom + ")/EffRateEntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_EffRateEntityGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get TaxBoxEffRates items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TaxBoxEffRates1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param EffectiveFrom Desc: EffectiveFrom   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxBoxEffRateRow
   */  
export function get_TaxRates_Company_TaxCode_RateCode_EffectiveFrom_TaxBoxEffRates(Company:string, TaxCode:string, RateCode:string, EffectiveFrom:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxBoxEffRateRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/TaxRates(" + Company + "," + TaxCode + "," + RateCode + "," + EffectiveFrom + ")/TaxBoxEffRates", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxBoxEffRateRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the TaxBoxEffRate item
   Description: Calls GetByID to retrieve the TaxBoxEffRate item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxBoxEffRate1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param EffectiveFrom Desc: EffectiveFrom   Required: True   Allow empty value : True
      @param BoxCode Desc: BoxCode   Required: True   Allow empty value : True
      @param SourceModule Desc: SourceModule   Required: True   Allow empty value : True
      @param AmountType Desc: AmountType   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxBoxEffRateRow
   */  
export function get_TaxRates_Company_TaxCode_RateCode_EffectiveFrom_TaxBoxEffRates_Company_TaxCode_RateCode_BoxCode_SourceModule_AmountType_ECAcquisitionSeq_EffectiveFrom(Company:string, TaxCode:string, RateCode:string, EffectiveFrom:string, BoxCode:string, SourceModule:string, AmountType:string, ECAcquisitionSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TaxBoxEffRateRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/TaxRates(" + Company + "," + TaxCode + "," + RateCode + "," + EffectiveFrom + ")/TaxBoxEffRates(" + Company + "," + TaxCode + "," + RateCode + "," + BoxCode + "," + SourceModule + "," + AmountType + "," + ECAcquisitionSeq + "," + EffectiveFrom + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_TaxBoxEffRateRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get TaxGRates items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TaxGRates1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param EffectiveFrom Desc: EffectiveFrom   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxGRateRow
   */  
export function get_TaxRates_Company_TaxCode_RateCode_EffectiveFrom_TaxGRates(Company:string, TaxCode:string, RateCode:string, EffectiveFrom:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxGRateRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/TaxRates(" + Company + "," + TaxCode + "," + RateCode + "," + EffectiveFrom + ")/TaxGRates", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxGRateRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the TaxGRate item
   Description: Calls GetByID to retrieve the TaxGRate item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxGRate1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param EffectiveFrom Desc: EffectiveFrom   Required: True   Allow empty value : True
      @param FromAmount Desc: FromAmount   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxGRateRow
   */  
export function get_TaxRates_Company_TaxCode_RateCode_EffectiveFrom_TaxGRates_Company_TaxCode_RateCode_EffectiveFrom_FromAmount(Company:string, TaxCode:string, RateCode:string, EffectiveFrom:string, FromAmount:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TaxGRateRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/TaxRates(" + Company + "," + TaxCode + "," + RateCode + "," + EffectiveFrom + ")/TaxGRates(" + Company + "," + TaxCode + "," + RateCode + "," + EffectiveFrom + "," + FromAmount + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_TaxGRateRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get EffRateEntityGLCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EffRateEntityGLCs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EffRateEntityGLCRow
   */  
export function get_EffRateEntityGLCs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EffRateEntityGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/EffRateEntityGLCs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EffRateEntityGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EffRateEntityGLCs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EffRateEntityGLCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.EffRateEntityGLCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EffRateEntityGLCs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/EffRateEntityGLCs", {
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
   Summary: Calls GetByID to retrieve the EffRateEntityGLC item
   Description: Calls GetByID to retrieve the EffRateEntityGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EffRateEntityGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param Key6 Desc: Key6   Required: True   Allow empty value : True
      @param GLControlType Desc: GLControlType   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EffRateEntityGLCRow
   */  
export function get_EffRateEntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, GLControlType:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_EffRateEntityGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/EffRateEntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_EffRateEntityGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update EffRateEntityGLC for the service
   Description: Calls UpdateExt to update EffRateEntityGLC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EffRateEntityGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param Key6 Desc: Key6   Required: True   Allow empty value : True
      @param GLControlType Desc: GLControlType   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.EffRateEntityGLCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_EffRateEntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, GLControlType:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/EffRateEntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
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
   Summary: Call UpdateExt to delete EffRateEntityGLC item
   Description: Call UpdateExt to delete EffRateEntityGLC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EffRateEntityGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param Key6 Desc: Key6   Required: True   Allow empty value : True
      @param GLControlType Desc: GLControlType   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_EffRateEntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, GLControlType:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/EffRateEntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
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
   Description: Get TaxBoxEffRates items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TaxBoxEffRates
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxBoxEffRateRow
   */  
export function get_TaxBoxEffRates(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxBoxEffRateRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/TaxBoxEffRates", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxBoxEffRateRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TaxBoxEffRates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TaxBoxEffRateRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TaxBoxEffRateRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TaxBoxEffRates(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/TaxBoxEffRates", {
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
   Summary: Calls GetByID to retrieve the TaxBoxEffRate item
   Description: Calls GetByID to retrieve the TaxBoxEffRate item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxBoxEffRate
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param BoxCode Desc: BoxCode   Required: True   Allow empty value : True
      @param SourceModule Desc: SourceModule   Required: True   Allow empty value : True
      @param AmountType Desc: AmountType   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      @param EffectiveFrom Desc: EffectiveFrom   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxBoxEffRateRow
   */  
export function get_TaxBoxEffRates_Company_TaxCode_RateCode_BoxCode_SourceModule_AmountType_ECAcquisitionSeq_EffectiveFrom(Company:string, TaxCode:string, RateCode:string, BoxCode:string, SourceModule:string, AmountType:string, ECAcquisitionSeq:string, EffectiveFrom:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TaxBoxEffRateRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/TaxBoxEffRates(" + Company + "," + TaxCode + "," + RateCode + "," + BoxCode + "," + SourceModule + "," + AmountType + "," + ECAcquisitionSeq + "," + EffectiveFrom + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_TaxBoxEffRateRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update TaxBoxEffRate for the service
   Description: Calls UpdateExt to update TaxBoxEffRate. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TaxBoxEffRate
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param BoxCode Desc: BoxCode   Required: True   Allow empty value : True
      @param SourceModule Desc: SourceModule   Required: True   Allow empty value : True
      @param AmountType Desc: AmountType   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      @param EffectiveFrom Desc: EffectiveFrom   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TaxBoxEffRateRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_TaxBoxEffRates_Company_TaxCode_RateCode_BoxCode_SourceModule_AmountType_ECAcquisitionSeq_EffectiveFrom(Company:string, TaxCode:string, RateCode:string, BoxCode:string, SourceModule:string, AmountType:string, ECAcquisitionSeq:string, EffectiveFrom:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/TaxBoxEffRates(" + Company + "," + TaxCode + "," + RateCode + "," + BoxCode + "," + SourceModule + "," + AmountType + "," + ECAcquisitionSeq + "," + EffectiveFrom + ")", {
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
   Summary: Call UpdateExt to delete TaxBoxEffRate item
   Description: Call UpdateExt to delete TaxBoxEffRate item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TaxBoxEffRate
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param BoxCode Desc: BoxCode   Required: True   Allow empty value : True
      @param SourceModule Desc: SourceModule   Required: True   Allow empty value : True
      @param AmountType Desc: AmountType   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      @param EffectiveFrom Desc: EffectiveFrom   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_TaxBoxEffRates_Company_TaxCode_RateCode_BoxCode_SourceModule_AmountType_ECAcquisitionSeq_EffectiveFrom(Company:string, TaxCode:string, RateCode:string, BoxCode:string, SourceModule:string, AmountType:string, ECAcquisitionSeq:string, EffectiveFrom:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/TaxBoxEffRates(" + Company + "," + TaxCode + "," + RateCode + "," + BoxCode + "," + SourceModule + "," + AmountType + "," + ECAcquisitionSeq + "," + EffectiveFrom + ")", {
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
   Description: Get TaxGRates items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TaxGRates
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxGRateRow
   */  
export function get_TaxGRates(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxGRateRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/TaxGRates", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxGRateRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TaxGRates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TaxGRateRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TaxGRateRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TaxGRates(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/TaxGRates", {
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
   Summary: Calls GetByID to retrieve the TaxGRate item
   Description: Calls GetByID to retrieve the TaxGRate item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxGRate
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param EffectiveFrom Desc: EffectiveFrom   Required: True   Allow empty value : True
      @param FromAmount Desc: FromAmount   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxGRateRow
   */  
export function get_TaxGRates_Company_TaxCode_RateCode_EffectiveFrom_FromAmount(Company:string, TaxCode:string, RateCode:string, EffectiveFrom:string, FromAmount:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TaxGRateRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/TaxGRates(" + Company + "," + TaxCode + "," + RateCode + "," + EffectiveFrom + "," + FromAmount + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_TaxGRateRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update TaxGRate for the service
   Description: Calls UpdateExt to update TaxGRate. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TaxGRate
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param EffectiveFrom Desc: EffectiveFrom   Required: True   Allow empty value : True
      @param FromAmount Desc: FromAmount   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TaxGRateRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_TaxGRates_Company_TaxCode_RateCode_EffectiveFrom_FromAmount(Company:string, TaxCode:string, RateCode:string, EffectiveFrom:string, FromAmount:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/TaxGRates(" + Company + "," + TaxCode + "," + RateCode + "," + EffectiveFrom + "," + FromAmount + ")", {
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
   Summary: Call UpdateExt to delete TaxGRate item
   Description: Call UpdateExt to delete TaxGRate item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TaxGRate
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param EffectiveFrom Desc: EffectiveFrom   Required: True   Allow empty value : True
      @param FromAmount Desc: FromAmount   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_TaxGRates_Company_TaxCode_RateCode_EffectiveFrom_FromAmount(Company:string, TaxCode:string, RateCode:string, EffectiveFrom:string, FromAmount:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/TaxGRates(" + Company + "," + TaxCode + "," + RateCode + "," + EffectiveFrom + "," + FromAmount + ")", {
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
   Description: Get PLSAFTCodes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PLSAFTCodes
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PLSAFTCodeRow
   */  
export function get_PLSAFTCodes(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PLSAFTCodeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/PLSAFTCodes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PLSAFTCodeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PLSAFTCodes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PLSAFTCodeRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PLSAFTCodeRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PLSAFTCodes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/PLSAFTCodes", {
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
   Summary: Calls GetByID to retrieve the PLSAFTCode item
   Description: Calls GetByID to retrieve the PLSAFTCode item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PLSAFTCode
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param SAFTCode Desc: SAFTCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PLSAFTCodeRow
   */  
export function get_PLSAFTCodes_Company_RateCode_TaxCode_SAFTCode(Company:string, RateCode:string, TaxCode:string, SAFTCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PLSAFTCodeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/PLSAFTCodes(" + Company + "," + RateCode + "," + TaxCode + "," + SAFTCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PLSAFTCodeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PLSAFTCode for the service
   Description: Calls UpdateExt to update PLSAFTCode. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PLSAFTCode
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param SAFTCode Desc: SAFTCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PLSAFTCodeRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PLSAFTCodes_Company_RateCode_TaxCode_SAFTCode(Company:string, RateCode:string, TaxCode:string, SAFTCode:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/PLSAFTCodes(" + Company + "," + RateCode + "," + TaxCode + "," + SAFTCode + ")", {
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
   Summary: Call UpdateExt to delete PLSAFTCode item
   Description: Call UpdateExt to delete PLSAFTCode item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PLSAFTCode
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param SAFTCode Desc: SAFTCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PLSAFTCodes_Company_RateCode_TaxCode_SAFTCode(Company:string, RateCode:string, TaxCode:string, SAFTCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/PLSAFTCodes(" + Company + "," + RateCode + "," + TaxCode + "," + SAFTCode + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SalesTaxListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SalesTaxListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SalesTaxListRow)
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
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
export function get_GetRows(whereClauseSalesTax:string, whereClauseLangDesc:string, whereClauseSalesTRC:string, whereClauseEntityGLC:string, whereClauseSalesTxc:string, whereClauseTaxBox:string, whereClauseTaxRate:string, whereClauseEffRateEntityGLC:string, whereClauseTaxBoxEffRate:string, whereClauseTaxGRate:string, whereClausePLSAFTCode:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseSalesTax!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseSalesTax=" + whereClauseSalesTax
   }
   if(typeof whereClauseLangDesc!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseLangDesc=" + whereClauseLangDesc
   }
   if(typeof whereClauseSalesTRC!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseSalesTRC=" + whereClauseSalesTRC
   }
   if(typeof whereClauseEntityGLC!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseEntityGLC=" + whereClauseEntityGLC
   }
   if(typeof whereClauseSalesTxc!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseSalesTxc=" + whereClauseSalesTxc
   }
   if(typeof whereClauseTaxBox!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseTaxBox=" + whereClauseTaxBox
   }
   if(typeof whereClauseTaxRate!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseTaxRate=" + whereClauseTaxRate
   }
   if(typeof whereClauseEffRateEntityGLC!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseEffRateEntityGLC=" + whereClauseEffRateEntityGLC
   }
   if(typeof whereClauseTaxBoxEffRate!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseTaxBoxEffRate=" + whereClauseTaxBoxEffRate
   }
   if(typeof whereClauseTaxGRate!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseTaxGRate=" + whereClauseTaxGRate
   }
   if(typeof whereClausePLSAFTCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePLSAFTCode=" + whereClausePLSAFTCode
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/GetRows" + params, {
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(taxCode:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof taxCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "taxCode=" + taxCode
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/GetList" + params, {
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
   Summary: Invoke method ChangeCollectionType
   Description: This method resets appropriate values when taxConnectCalc is true.
   OperationID: ChangeCollectionType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCollectionType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCollectionType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCollectionType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/ChangeCollectionType", {
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
   Summary: Invoke method ChangeDiscountType
   Description: This method resets appropriate values when taxConnectCalc is true.
   OperationID: ChangeDiscountType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDiscountType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDiscountType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDiscountType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/ChangeDiscountType", {
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
   Summary: Invoke method ChangeTaxBoxCode
   Description: This method validates BoxCode entered and populates the record from TaxBoxDefault.
   OperationID: ChangeTaxBoxCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTaxBoxCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTaxBoxCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTaxBoxCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/ChangeTaxBoxCode", {
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
   Summary: Invoke method ChangeTaxConnectCalc
   Description: This method resets appropriate values when taxConnectCalc is true.
   OperationID: ChangeTaxConnectCalc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTaxConnectCalc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTaxConnectCalc_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTaxConnectCalc(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/ChangeTaxConnectCalc", {
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
   Summary: Invoke method ChangeNumbering
   Description: This method validates wrong values.
   OperationID: ChangeNumbering
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeNumbering_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeNumbering_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeNumbering(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/ChangeNumbering", {
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
   Summary: Invoke method ChangeTiming
   Description: This method resets appropriate values ServiceTaxPoint when Timing is 0.
   OperationID: ChangeTiming
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTiming_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTiming_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTiming(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/ChangeTiming", {
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
   Summary: Invoke method ChangeDescription
   OperationID: ChangeDescription
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDescription_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDescription_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDescription(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/ChangeDescription", {
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
   Description: This method checks if Rate Type selected is valid for selected Collection Method.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/ChangeRateType", {
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
   Summary: Invoke method GetNewEffRateEntityGLCOver
   Description: This method used to get new EffRateEntityGLC with proper key values.
   OperationID: GetNewEffRateEntityGLCOver
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEffRateEntityGLCOver_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEffRateEntityGLCOver_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewEffRateEntityGLCOver(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/GetNewEffRateEntityGLCOver", {
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
   Summary: Invoke method ValidateEffectiveDate
   Description: Validate Tax Rate's Effective Date and return a true if effective rate exists for this date.
   OperationID: ValidateEffectiveDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateEffectiveDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateEffectiveDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateEffectiveDate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/ValidateEffectiveDate", {
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
   Summary: Invoke method GetNewTaxBoxEffRateOver
   Description: This method used to get new TaxBoxEffRate with proper key values.
   OperationID: GetNewTaxBoxEffRateOver
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTaxBoxEffRateOver_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTaxBoxEffRateOver_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewTaxBoxEffRateOver(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/GetNewTaxBoxEffRateOver", {
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
   Summary: Invoke method ChangeTaxBoxEffRateCode
   Description: This method validates BoxCode entered and populates the record from TaxBoxDefault.
   OperationID: ChangeTaxBoxEffRateCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTaxBoxEffRateCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTaxBoxEffRateCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTaxBoxEffRateCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/ChangeTaxBoxEffRateCode", {
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
   Summary: Invoke method CopyTaxBoxEffFromLastEffRate
   Description: Copy TaxBoxEffRate from Last Effective Tax Rate
   OperationID: CopyTaxBoxEffFromLastEffRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CopyTaxBoxEffFromLastEffRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyTaxBoxEffFromLastEffRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CopyTaxBoxEffFromLastEffRate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/CopyTaxBoxEffFromLastEffRate", {
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
   Summary: Invoke method CopyTaxBoxFromRatesTaxBox
   Description: Copy TaxBoxEffRate from Rates > Tax Boxes
   OperationID: CopyTaxBoxFromRatesTaxBox
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CopyTaxBoxFromRatesTaxBox_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyTaxBoxFromRatesTaxBox_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CopyTaxBoxFromRatesTaxBox(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/CopyTaxBoxFromRatesTaxBox", {
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
   Summary: Invoke method DisableCopyTaxBoxFromLastEffRate
   OperationID: DisableCopyTaxBoxFromLastEffRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DisableCopyTaxBoxFromLastEffRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DisableCopyTaxBoxFromLastEffRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DisableCopyTaxBoxFromLastEffRate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/DisableCopyTaxBoxFromLastEffRate", {
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
   Summary: Invoke method DisableCopyTaxBoxFromRates
   OperationID: DisableCopyTaxBoxFromRates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DisableCopyTaxBoxFromRates_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DisableCopyTaxBoxFromRates_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DisableCopyTaxBoxFromRates(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/DisableCopyTaxBoxFromRates", {
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
   Summary: Invoke method CheckPLSAFTCode
   Description: SAF-T code validation
   OperationID: CheckPLSAFTCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPLSAFTCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPLSAFTCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPLSAFTCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/CheckPLSAFTCode", {
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
   Summary: Invoke method CheckPLSAFTCodeAndDescUpdate
   Description: SAF-T code validation and description getting
   OperationID: CheckPLSAFTCodeAndDescUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPLSAFTCodeAndDescUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPLSAFTCodeAndDescUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPLSAFTCodeAndDescUpdate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/CheckPLSAFTCodeAndDescUpdate", {
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
   Summary: Invoke method UpdatePLSAFTCode
   OperationID: UpdatePLSAFTCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdatePLSAFTCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdatePLSAFTCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdatePLSAFTCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/UpdatePLSAFTCode", {
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
   Summary: Invoke method LookupPLSAFTCode
   OperationID: LookupPLSAFTCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LookupPLSAFTCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LookupPLSAFTCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LookupPLSAFTCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/LookupPLSAFTCode", {
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
   Summary: Invoke method RemovePLSAFTCode
   OperationID: RemovePLSAFTCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RemovePLSAFTCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RemovePLSAFTCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RemovePLSAFTCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/RemovePLSAFTCode", {
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
   Summary: Invoke method PEChangeUDCode
   Description: This method should be called after SUNAT fields have been changed.
   OperationID: PEChangeUDCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PEChangeUDCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PEChangeUDCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PEChangeUDCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/PEChangeUDCode", {
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
   Summary: Invoke method PEChangeType
   Description: This method should be called after Type field has been changed.
   OperationID: PEChangeType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PEChangeType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PEChangeType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PEChangeType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/PEChangeType", {
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
   Summary: Invoke method GetTimingDataForCombo
   OperationID: GetTimingDataForCombo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTimingDataForCombo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTimingDataForCombo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTimingDataForCombo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/GetTimingDataForCombo", {
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
   Summary: Invoke method GetCollectionDataForCombo
   Description: Get Data for Collection combobox
   OperationID: GetCollectionDataForCombo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCollectionDataForCombo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCollectionDataForCombo(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/GetCollectionDataForCombo", {
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
   Summary: Invoke method GetRateTypes
   Description: Get Data for Effective Rate Rate Types combo.
   OperationID: GetRateTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRateTypes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRateTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRateTypes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/GetRateTypes", {
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
   Summary: Invoke method GetDiscountTypes
   Description: Get data for Discount types combo.
   OperationID: GetDiscountTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDiscountTypes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDiscountTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDiscountTypes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/GetDiscountTypes", {
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
   Summary: Invoke method GetNumberingValues
   Description: Get data fo Numbering combo
   OperationID: GetNumberingValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNumberingValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNumberingValues(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/GetNumberingValues", {
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
   Summary: Invoke method GetNewSalesTax
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSalesTax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSalesTax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSalesTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewSalesTax(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/GetNewSalesTax", {
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
   Summary: Invoke method GetNewLangDesc
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLangDesc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLangDesc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLangDesc_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewLangDesc(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/GetNewLangDesc", {
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
   Summary: Invoke method GetNewSalesTRC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSalesTRC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSalesTRC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSalesTRC_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewSalesTRC(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/GetNewSalesTRC", {
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
   Summary: Invoke method GetNewEntityGLC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEntityGLC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEntityGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEntityGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewEntityGLC(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/GetNewEntityGLC", {
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
   Summary: Invoke method GetNewSalesTxc
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSalesTxc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSalesTxc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSalesTxc_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewSalesTxc(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/GetNewSalesTxc", {
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
   Summary: Invoke method GetNewTaxBox
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTaxBox
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTaxBox_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTaxBox_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewTaxBox(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/GetNewTaxBox", {
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
   Summary: Invoke method GetNewTaxRate
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTaxRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTaxRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTaxRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewTaxRate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/GetNewTaxRate", {
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
   Summary: Invoke method GetNewEffRateEntityGLC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEffRateEntityGLC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEffRateEntityGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEffRateEntityGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewEffRateEntityGLC(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/GetNewEffRateEntityGLC", {
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
   Summary: Invoke method GetNewTaxBoxEffRate
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTaxBoxEffRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTaxBoxEffRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTaxBoxEffRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewTaxBoxEffRate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/GetNewTaxBoxEffRate", {
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
   Summary: Invoke method GetNewTaxGRate
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTaxGRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTaxGRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTaxGRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewTaxGRate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/GetNewTaxGRate", {
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
   Summary: Invoke method GetNewPLSAFTCode
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPLSAFTCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPLSAFTCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPLSAFTCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPLSAFTCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/GetNewPLSAFTCode", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EffRateEntityGLCRow{
   "odatametadata":string,
   "value":Erp_Tablesets_EffRateEntityGLCRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow{
   "odatametadata":string,
   "value":Erp_Tablesets_EntityGLCRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LangDescRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LangDescRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PLSAFTCodeRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PLSAFTCodeRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SalesTRCRow{
   "odatametadata":string,
   "value":Erp_Tablesets_SalesTRCRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SalesTaxListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_SalesTaxListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SalesTaxRow{
   "odatametadata":string,
   "value":Erp_Tablesets_SalesTaxRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SalesTxcRow{
   "odatametadata":string,
   "value":Erp_Tablesets_SalesTxcRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxBoxEffRateRow{
   "odatametadata":string,
   "value":Erp_Tablesets_TaxBoxEffRateRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxBoxRow{
   "odatametadata":string,
   "value":Erp_Tablesets_TaxBoxRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxGRateRow{
   "odatametadata":string,
   "value":Erp_Tablesets_TaxGRateRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxRateRow{
   "odatametadata":string,
   "value":Erp_Tablesets_TaxRateRow[],
}

export interface Erp_Tablesets_EffRateEntityGLCRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  */  
   "RelatedToFile":string,
      /**  Major component of the foreign key of the related master record. For example: For a "Part"  control this field would contain the related Part Number,  for a "Customer"  it contains the Customer.CustNum.  */  
   "Key1":string,
      /**   2nd component of the foreign key to the related master record.
The usage of this field is dependent on the type of record.  */  
   "Key2":string,
      /**   3rd component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key3":string,
      /**   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key4":string,
      /**   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key5":string,
      /**   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key6":string,
      /**  Identifier of the GL Control Type.  */  
   "GLControlType":string,
      /**  GL Control Identifier.  */  
   "GLControlCode":string,
      /**  Identifies the entity.  Reference only.  Used for integrity validation when deleting a GLCTEntity record.  */  
   "BusinessEntity":string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   "ExtCompanyID":string,
      /**  Flag to indicate the account in this record is for an external company.  */  
   "IsExternalCompany":boolean,
      /**  Marks this EntityGLC as global, available to be sent out to other companies.  */  
   "GlobalEntityGLC":boolean,
      /**  Disables this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "TaxCode":string,
   "RateCode":string,
   "EffectiveFrom":string,
   "BitFlag":number,
   "GLCntrlDescription":string,
   "GLCntrlTypeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_EntityGLCRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  */  
   "RelatedToFile":string,
      /**  Major component of the foreign key of the related master record. For example: For a "Part"  control this field would contain the related Part Number,  for a "Customer"  it contains the Customer.CustNum.  */  
   "Key1":string,
      /**   2nd component of the foreign key to the related master record.
The usage of this field is dependent on the type of record.  */  
   "Key2":string,
      /**   3rd component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key3":string,
      /**   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key4":string,
      /**   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key5":string,
      /**   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key6":string,
      /**  Identifier of the GL Control Type.  */  
   "GLControlType":string,
      /**  GL Control Identifier.  */  
   "GLControlCode":string,
      /**  Identifies the entity.  Reference only.  Used for integrity validation when deleting a GLCTEntity record.  */  
   "BusinessEntity":string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   "ExtCompanyID":string,
      /**  Flag to indicate the account in this record is for an external company.  */  
   "IsExternalCompany":boolean,
      /**  Marks this EntityGLC as global, available to be sent out to other companies.  */  
   "GlobalEntityGLC":boolean,
      /**  Disables this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  BankAcctID of the related BankAcct record.  */  
   "BankAcctID":string,
   "BankFeeID":string,
      /**  CallCode of the related FSCallCd record.  */  
   "CallCode":string,
   "ChargeCode":string,
      /**  ClassCode of the related FAClass record.  */  
   "ClassCode":string,
      /**  ClassID.  This can be ClassID of PartClass, PRClsDed, or PRClsTax  */  
   "ClassID":string,
      /**  ContractCode of the related FSContCd record.  */  
   "ContractCode":string,
      /**  CurrencyCode of the related Currency record.  */  
   "CurrencyCode":string,
      /**  CustNum of the related Customer record  */  
   "CustNum":number,
      /**  DeductionID of PRClsDed or PRDeduct.  */  
   "DeductionID":string,
      /**  EmpID of the related PREmpMas record.  */  
   "EmpID":string,
      /**  ExpenseCode of PayTLbr, LabExpCd  */  
   "ExpenseCode":string,
      /**  ExtSystemID of ExtCompany table  */  
   "ExtSystemID":string,
      /**  FromPlant value of the related PlntTranDef record.  */  
   "FromPlant":string,
      /**  GroupCode of the related FAGroup record.  */  
   "GroupCode":string,
   "GroupID":string,
   "HeadNum":number,
   "InvoiceNum":string,
      /**  JCDept of the related JCDept record.  */  
   "JCDept":string,
      /**  MiscCode of the related MiscChrg or PurMisc record.  */  
   "MiscCode":string,
      /**  PartNum of the related Part record.  */  
   "PartNum":string,
      /**  PayTypeID of PayType  */  
   "PayTypeID":string,
   "PerConName":string,
      /**  PI Status  */  
   "PIStatus":string,
      /**  Plant of the related PlantConfCtrl record.  */  
   "Plant":string,
      /**  ProdCode of the related ProdGrup record.  */  
   "ProdCode":string,
      /**  ProjectID of the related Project record.  */  
   "ProjectID":string,
      /**  PurchCode of the related GLPurch record.  */  
   "PurchCode":string,
      /**  RateCode of the related GLRate record.  */  
   "RateCode":string,
      /**  ReasonCode of the related Reason record.  */  
   "ReasonCode":string,
      /**  ReasonType of the related Reason record.  */  
   "ReasonType":string,
      /**  SalesCatID of the related SalesCat record.  */  
   "SalesCatID":string,
      /**  Shift value of the related JCShift record.  */  
   "Shift":number,
      /**  TaxCode of the related SalesTax record.  */  
   "TaxCode":string,
      /**  TaxTblID of PRTaxMas or PRClsTax.  */  
   "TaxTblID":string,
      /**  ToPlant value of the related PlntTranDef record.  */  
   "ToPlant":string,
      /**  TransferMethod of ExtCompany table  */  
   "TransferMethod":string,
      /**  Type ID  */  
   "TypeID":string,
      /**  VendorNum of the related Vendor record.  */  
   "VendorNum":number,
      /**  WarehouseCode of the related Warehse record.  */  
   "WarehouseCode":string,
   "ExpenseTypeCode":string,
   "IsFiltered":boolean,
   "OprTypeCode":string,
   "CashDeskID":string,
   "TIN":string,
   "ReclassCodeID":string,
   "BitFlag":number,
   "GLCntrlDescription":string,
   "GLCntrlTypeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_LangDescRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Name of table that this data is related  */  
   "TableName":string,
      /**  Language ID  */  
   "LangNameID":string,
      /**  Contains values that represent the key1 to the foreign record that this record is related.  */  
   "Key1":string,
      /**  key2  of  the foreign record  */  
   "Key2":string,
      /**  key3 of the foreign record  */  
   "Key3":string,
      /**  Language Description  */  
   "Description":string,
      /**  Marks this LangDesc as global, available to be sent out to other companies.  */  
   "GlobalLangDesc":boolean,
      /**  Disables this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "LangNameIDDescription":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PLSAFTCodeRow{
      /**  Company  */  
   "Company":string,
      /**  RateCode  */  
   "RateCode":string,
      /**  TaxCode  */  
   "TaxCode":string,
      /**  SAFTCode  */  
   "SAFTCode":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "CodeDesc":string,
   "LongDesc":string,
   "TempSAFTCode":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_SalesTRCRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "TaxCode":string,
      /**  Rate Code  */  
   "RateCode":string,
      /**  Description  */  
   "Description":string,
      /**  Default Rate  */  
   "DefaultRate":boolean,
      /**  Legal Text code  */  
   "TextCode":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  AGAFIPCode  */  
   "AGAFIPCode":string,
      /**  AGFEAFIPCode  */  
   "AGFEAFIPCode":string,
      /**  AGPurchaseColNumber  */  
   "AGPurchaseColNumber":number,
      /**  AGSalesColNumber  */  
   "AGSalesColNumber":number,
      /**  Intracom Code (CSF Belgium)  */  
   "BEIntracomCode":string,
      /**  JPConsumptionTax  */  
   "JPConsumptionTax":boolean,
      /**  PLSAFTCode  */  
   "PLSAFTCode":string,
      /**  CODIANCode  */  
   "CODIANCode":string,
      /**  UNCL5305  */  
   "ExternalTaxCategory":string,
      /**  Indicate if is tring to be deleted from SalesTax  */  
   "FatherDeleted":boolean,
   "BitFlag":number,
   "TaxTextDescription":string,
   "XbSystELIEinvoice":boolean,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_SalesTaxListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "TaxCode":string,
      /**  Full description for a  Sales Tax master.  */  
   "Description":string,
      /**  Indicates if the tax calculations are to be performed manually.  This field is used as a default for the InvcTax.Manual field.  When this field is set in the InvcTax record the InvcTax.Reportable, InvcTax.TaxableAmt, and InvcTax.TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations automatically.  */  
   "Manual":boolean,
      /**  Indicates if set to Yes that any decimal values of a penny/cent should be rounded down rather than rounded to nearest penny/cent.  */  
   "RoundDown":boolean,
      /**  When checked the sales tax code will apply to advanced billing invoices, and will only apply to additional sums on final invoices.  */  
   "Advanced":boolean,
      /**  Indicates whether taxes related to this Sales Tax ID are calculated via Epicor Tax Connect interface. Default is No.  */  
   "TaxConnectCalc":boolean,
      /**  If this SalesTax id is used by TaxConnect, this is a string containing the data required to uniquely identify a specific taxing jurisdiction using the tax connect system data. It will be used to generate the ETCHash field. If multiple fields from the tax connect system are required to generate a unique key, they should be concatenated, separated by ?:?. For Avalara it will be the StateJurisCode+ ?:? + TaxDetail JurisCode + ?:? + TaxDetail JurisName returned by the GetTax function for each tax amount. Default is null.  */  
   "ETCJurisKey":string,
      /**  If this SalesTax id is used by TaxConnect, this is the hash field to be used to cross reference the key fields provided by the tax connect service (stored in ETCJurisKey)  with the Epicor SalesTax id of this record in order to obtain the correct tax accrual GLs for the transaction. Default is null.  */  
   "ETCHash":number,
      /**  Collection Type  */  
   "CollectionType":number,
      /**  Timing of when to report taxes (default)  */  
   "Timing":number,
      /**  Algorithm  */  
   "Algorithm":string,
      /**  Discount Types, none, payment discount affect tax, terms discount affect tax  */  
   "DiscountType":number,
      /**  Tax Jurisdiction  */  
   "TaxJurisCode":string,
      /**  Tax Report Category  */  
   "RptCatCode":string,
      /**  Legal Text Code  */  
   "TextCode":string,
      /**  In Price  */  
   "InPrice":boolean,
      /**  Tax Certificate Numbering method  */  
   "LglNumType":number,
      /**  Legal Number Sequence  */  
   "LglNumSeq":number,
      /**  Reverse Tax Report Category  */  
   "RevRptCatCode":string,
      /**  Intra-EU Service  */  
   "ServiceTaxPoint":boolean,
      /**  Sales List Type Indicator  */  
   "Direct":string,
      /**  Sales List Type Indicator  */  
   "Triangulation":string,
      /**  Marks this SalesTax as global, available to be sent out to other companies.  */  
   "GlobalSalesTax":boolean,
      /**  Disables this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  Invoice Type: 0-No Vat Reporting, 1-Tax Invoice, 2-Duty-Free Invoice  */  
   "InvoiceType":string,
      /**  Invoicing Method: 0-No VAT Reporting, 1-Paper Invoice, 2-eInvoice, 3-No Invoice  */  
   "InvMethod":string,
      /**  Customer Type: 0-No VAT Reporting, 1-Company Sales, 2-Personal Sales  */  
   "CustType":string,
      /**  Revenue Type: 0-No VAT Reporting, 1-Trading Revenue, 2-Non-Trading Revenue  */  
   "RevType":string,
      /**  Issue Type: 0-No VAT Reporting, 1-Normal Invoice, 2-Issued by Supplier  */  
   "IssueType":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Parent Tax Id  */  
   "ParentJurisdiction":string,
      /**  Flag to indicate if Reverse Charge should be enabled.  */  
   "EnableRevCharge":boolean,
      /**  Flag to indicate if Tax Box maintenance should be allowed.  */  
   "EnableTaxBox":boolean,
      /**  Description of the record, translated in the selected language  */  
   "mtlDescription":string,
      /**  Name of the selected language of Description  */  
   "mtlLangDesc":string,
      /**  ID of the selected language  */  
   "mtlLangId":string,
      /**  Description  */  
   "TaxAlgrmDescription":string,
      /**  Description  */  
   "TaxJurisDescription":string,
      /**  Description  */  
   "TaxRptCatDescription":string,
      /**  Description  */  
   "TaxTextDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_SalesTaxRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "TaxCode":string,
      /**  Full description for a  Sales Tax master.  */  
   "Description":string,
      /**  Indicates if the tax calculations are to be performed manually.  This field is used as a default for the InvcTax.Manual field.  When this field is set in the InvcTax record the InvcTax.Reportable, InvcTax.TaxableAmt, and InvcTax.TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations automatically.  */  
   "Manual":boolean,
      /**  Indicates if set to Yes that any decimal values of a penny/cent should be rounded down rather than rounded to nearest penny/cent.  */  
   "RoundDown":boolean,
      /**  When checked the sales tax code will apply to advanced billing invoices, and will only apply to additional sums on final invoices.  */  
   "Advanced":boolean,
      /**  Indicates whether taxes related to this Sales Tax ID are calculated via Epicor Tax Connect interface. Default is No.  */  
   "TaxConnectCalc":boolean,
      /**  If this SalesTax id is used by TaxConnect, this is a string containing the data required to uniquely identify a specific taxing jurisdiction using the tax connect system data. It will be used to generate the ETCHash field. If multiple fields from the tax connect system are required to generate a unique key, they should be concatenated, separated by ?:?. For Avalara it will be the StateJurisCode+ ?:? + TaxDetail JurisCode + ?:? + TaxDetail JurisName returned by the GetTax function for each tax amount. Default is null.  */  
   "ETCJurisKey":string,
      /**  If this SalesTax id is used by TaxConnect, this is the hash field to be used to cross reference the key fields provided by the tax connect service (stored in ETCJurisKey)  with the Epicor SalesTax id of this record in order to obtain the correct tax accrual GLs for the transaction. Default is null.  */  
   "ETCHash":number,
      /**  Collection Type  */  
   "CollectionType":number,
      /**  Timing of when to report taxes (default)  */  
   "Timing":number,
      /**  Algorithm  */  
   "Algorithm":string,
      /**  Discount Types, none, payment discount affect tax, terms discount affect tax  */  
   "DiscountType":number,
      /**  Tax Jurisdiction  */  
   "TaxJurisCode":string,
      /**  Tax Report Category  */  
   "RptCatCode":string,
      /**  Legal Text Code  */  
   "TextCode":string,
      /**  In Price  */  
   "InPrice":boolean,
      /**  Tax Certificate Numbering method  */  
   "LglNumType":number,
      /**  Legal Number Sequence  */  
   "LglNumSeq":number,
      /**  Reverse Tax Report Category  */  
   "RevRptCatCode":string,
      /**  Intra-EU Service  */  
   "ServiceTaxPoint":boolean,
      /**  Sales List Type Indicator  */  
   "Direct":string,
      /**  Sales List Type Indicator  */  
   "Triangulation":string,
      /**  Marks this SalesTax as global, available to be sent out to other companies.  */  
   "GlobalSalesTax":boolean,
      /**  Disables this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  Invoice Type: 0-No Vat Reporting, 1-Tax Invoice, 2-Duty-Free Invoice  */  
   "InvoiceType":string,
      /**  Invoicing Method: 0-No VAT Reporting, 1-Paper Invoice, 2-eInvoice, 3-No Invoice  */  
   "InvMethod":string,
      /**  Customer Type: 0-No VAT Reporting, 1-Company Sales, 2-Personal Sales  */  
   "CustType":string,
      /**  Revenue Type: 0-No VAT Reporting, 1-Trading Revenue, 2-Non-Trading Revenue  */  
   "RevType":string,
      /**  Issue Type: 0-No VAT Reporting, 1-Normal Invoice, 2-Issued by Supplier  */  
   "IssueType":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  INIsCST  */  
   "INIsCST":boolean,
      /**  AGAFIPCode  */  
   "AGAFIPCode":string,
      /**  AGAFIPTaxRegCode  */  
   "AGAFIPTaxRegCode":string,
      /**  AGAFIPTaxRegDesc  */  
   "AGAFIPTaxRegDesc":string,
      /**  AGMinimumByTax  */  
   "AGMinimumByTax":boolean,
      /**  AGTaxableAmtType  */  
   "AGTaxableAmtType":string,
      /**  AGWHHeader  */  
   "AGWHHeader":string,
      /**  IndirectTaxType  */  
   "IndirectTaxType":string,
      /**  Mexico Localizaion field to store TaxType Category for Mexico  */  
   "MXTaxCategory":string,
      /**  NOTaxCategory  */  
   "NOTaxCategory":string,
      /**  PETranDocTypeID  */  
   "PETranDocTypeID":string,
      /**  PETaxOriginType  */  
   "PETaxOriginType":string,
      /**  MXSATCode  */  
   "MXSATCode":string,
      /**  PE SUNAT Code  */  
   "PESUNATCode":string,
      /**  PE SUNAT Name  */  
   "PESUNATName":string,
      /**  PE SUNAT Type  */  
   "PESUNATType":string,
      /**  PLSAFTCode  */  
   "PLSAFTCode":string,
      /**  MXTaxType  */  
   "MXTaxType":string,
      /**  MXTypeFactor  */  
   "MXTypeFactor":string,
      /**  Determines if the tax type has to be synchronized with Epicor FSA application.  */  
   "SendToFSA":boolean,
      /**  Timing of when to report taxes (specific to Deposit Billing and Advanced Billing invoices)  */  
   "TimingDepositAdvBilling":number,
      /**  E-Invoice Tax Category  */  
   "EInvTaxCategory":string,
      /**  PEISCCalcCode  */  
   "PEISCCalcCode":string,
      /**  PEAllowanceChargeReasonCode  */  
   "PEAllowanceChargeReasonCode":string,
      /**  Tax category; Country specific, e.g. ‘GST’ for ANZ. UNTDID 5153  */  
   "ExternalTaxCategory":string,
   "AllowConfirmationTax":boolean,
      /**  Flag to indicate if Reverse Charge should be enabled.  */  
   "EnableRevCharge":boolean,
      /**  Flag to indicate if Tax Box maintenance should be allowed.  */  
   "EnableTaxBox":boolean,
      /**  Description of the record, translated in the selected language  */  
   "mtlDescription":string,
      /**  Name of the selected language of Description  */  
   "mtlLangDesc":string,
      /**  ID of the selected language  */  
   "mtlLangId":string,
      /**  Parent Tax Id  */  
   "ParentJurisdiction":string,
   "PEISCCalcCodeDesc":string,
   "PESUNATCodeDesc":string,
      /**  Flag to indicate if the tax type is assigned to a tax liability.  */  
   "EnableChanges":boolean,
      /**  Peru CSF: Allowance Change Reason Code description  */  
   "PEAllowanceChargeReasonDesc":string,
   "BitFlag":number,
   "CompanySendToFSA":boolean,
   "TaxAlgrmDescription":string,
   "TaxJurisDescription":string,
   "TaxRptCatDescription":string,
   "TaxTextDescription":string,
   "XbSystELIEinvoice":boolean,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_SalesTxcRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The TaxCode to which this record is related.  */  
   "TaxCode":string,
      /**  The TaxCatID which relates this record to the TaxCat record.  */  
   "TaxCatID":string,
      /**  Indicates that sales made of tax category are still reportable to the taxing jurisdiction as gross receipts even thou this category is  not  taxable.  */  
   "Reportable":boolean,
      /**  Rate Code  */  
   "RateCode":string,
      /**  Exemption Type  */  
   "ExemptType":number,
      /**  Exemption Percent  */  
   "ExemptPercent":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Tax category description  */  
   "TaxCatIDDesc":string,
   "BitFlag":number,
   "TaxCatIDDescription":string,
   "TaxCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_TaxBoxEffRateRow{
      /**  Company  */  
   "Company":string,
      /**  TaxCode  */  
   "TaxCode":string,
      /**  BoxCode  */  
   "BoxCode":string,
      /**  SourceModule  */  
   "SourceModule":string,
      /**  AmountType  */  
   "AmountType":string,
      /**  ECAcquisitionSeq  */  
   "ECAcquisitionSeq":number,
      /**  EffectiveFrom  */  
   "EffectiveFrom":string,
      /**  BoxSign  */  
   "BoxSign":string,
      /**  RateCode  */  
   "RateCode":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  Box Code Description  */  
   "BoxCodeDescription":string,
      /**  Flag to indicate if Tax Box maintenance should be allowed.  */  
   "EnableTaxBox":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_TaxBoxRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "TaxCode":string,
      /**  Tax Box Code.  */  
   "BoxCode":string,
      /**   Indicates the source module of the transaction for this tax box.
Possible values are: "AR" = from AR Invoice;  "AP" = from AP Invoice;  "ARCM" = from AR Credit Memo;  "APDM" = from AP Debit Memo.  */  
   "SourceModule":string,
      /**  The Amount type to be stored for this tax box.  The possible values are:  "Tax" = for Tax Amount; "Taxable" = for Taxable Amount.  */  
   "AmountType":string,
      /**  Indicates if the tax line associated with this tax box is the Primary or Secondary line. This field corresponds to the ECAcquisitionSeq stored in the APInvTax to indicate the second reversing tax line.  Valid values are: 0 = Primary or Standard tax line;  1 = Secondary or Reversing tax line (only created if ECAcquisition or Reverse Charge apply)  */  
   "ECAcquisitionSeq":number,
      /**  Sign for box amount. + means add the taxable/tax amount to the (taxable/tax) box value; - means substract the taxable/tax amount from the (taxable/tax) box value.  */  
   "BoxSign":string,
      /**  Rate Code  */  
   "RateCode":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Flag to indicate if Tax Box maintenance should be allowed.  */  
   "EnableTaxBox":boolean,
      /**  Box Code Description  */  
   "BoxCodeDescription":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_TaxGRateRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "TaxCode":string,
      /**  Tax Rate Code  */  
   "RateCode":string,
      /**  First date tax rate is valid for  */  
   "EffectiveFrom":string,
      /**  Minimum amount to apply tax to  */  
   "FromAmount":number,
      /**  Tax Percent to use  */  
   "TaxPercent":number,
      /**  Fixed Tax Amount to apply  */  
   "TaxAmount":number,
      /**  Reverse Charge  */  
   "ReverseCharge":boolean,
      /**  Unique Identifier for Legal Text  */  
   "TextCode":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Flag to indicate if Reverse Charge check box is available to the user  */  
   "ReverseAvail":boolean,
   "CurrencyCode":string,
   "BitFlag":number,
   "TaxTextDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_TaxRateRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "TaxCode":string,
      /**  Rate Code  */  
   "RateCode":string,
      /**  First date tax rate is valid for  */  
   "EffectiveFrom":string,
      /**  Percentage, Fixed Value or Graduated Rate  */  
   "RateType":number,
      /**  Tax Percent  */  
   "TaxPercent":number,
      /**  Fixed Tax Amount  */  
   "TaxAmount":number,
      /**  Deduction Percent  */  
   "DeductPercent":number,
      /**  Currency Code  */  
   "CurrencyCode":string,
      /**  Minimum Amount  */  
   "MinAmount":number,
      /**  Maximum Amount  */  
   "MaxAmount":number,
      /**  Cent Override Code  */  
   "CentCode":string,
      /**  I - Document Level, L - Line Level  */  
   "CompMethod":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  PEMinInvAmt  */  
   "PEMinInvAmt":number,
      /**  PEMinPayAmt  */  
   "PEMinPayAmt":number,
      /**  PEIncTaxAmt  */  
   "PEIncTaxAmt":boolean,
      /**  PEWHCurrencyCode  */  
   "PEWHCurrencyCode":string,
      /**  Indicates if Deduct percent is not available for changes (always 100%)  */  
   "DisableDeduct":boolean,
      /**  PatchField for TaxPercent (using 3 decimals instead of 2)  */  
   "DspTaxPercent":number,
      /**  Enable copy Tax Boxes from Last Effective Rate  */  
   "EnableCopyTaxBoxFromLEffRate":boolean,
      /**  Enable button copy Tax Boxes from Tax Rate Boxes  */  
   "EnableCopyTaxBoxFromRates":boolean,
      /**  Like SalesTax.CollectionType - for technical purpose  */  
   "CollectionType":number,
   "BitFlag":number,
   "CurrencyCurrName":string,
   "CurrencyDocumentDesc":string,
   "CurrencyCurrDesc":string,
   "CurrencyCurrencyID":string,
   "CurrencyCurrSymbol":string,
   "TaxCentDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param proposedCollectionType
      @param ds
   */  
export interface ChangeCollectionType_input{
      /**  The proposed Tax Collection Type.  */  
   proposedCollectionType:number,
   ds:Erp_Tablesets_SalesTaxTableset[],
}

export interface ChangeCollectionType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SalesTaxTableset[],
}
}

   /** Required : 
      @param Description
      @param ds
   */  
export interface ChangeDescription_input{
   Description:string,
   ds:Erp_Tablesets_SalesTaxTableset[],
}

export interface ChangeDescription_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SalesTaxTableset[],
}
}

   /** Required : 
      @param proposedDiscountType
      @param ds
   */  
export interface ChangeDiscountType_input{
      /**  The proposed Discount Type value.  */  
   proposedDiscountType:number,
   ds:Erp_Tablesets_SalesTaxTableset[],
}

export interface ChangeDiscountType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SalesTaxTableset[],
}
}

   /** Required : 
      @param proposedNumbering
      @param ds
   */  
export interface ChangeNumbering_input{
      /**  The proposed Numbering.  */  
   proposedNumbering:number,
   ds:Erp_Tablesets_SalesTaxTableset[],
}

export interface ChangeNumbering_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SalesTaxTableset[],
}
}

   /** Required : 
      @param ds
      @param proposedRateType
   */  
export interface ChangeRateType_input{
   ds:Erp_Tablesets_SalesTaxTableset[],
      /**  The proposed Rate Type.  */  
   proposedRateType:number,
}

export interface ChangeRateType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SalesTaxTableset[],
}
}

   /** Required : 
      @param proposedBoxCode
      @param ds
   */  
export interface ChangeTaxBoxCode_input{
      /**  The proposed BoxCode value.  */  
   proposedBoxCode:string,
   ds:Erp_Tablesets_SalesTaxTableset[],
}

export interface ChangeTaxBoxCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SalesTaxTableset[],
}
}

   /** Required : 
      @param proposedBoxCode
      @param ds
   */  
export interface ChangeTaxBoxEffRateCode_input{
      /**  The proposed BoxCode value.  */  
   proposedBoxCode:string,
   ds:Erp_Tablesets_SalesTaxTableset[],
}

export interface ChangeTaxBoxEffRateCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SalesTaxTableset[],
}
}

   /** Required : 
      @param proposedTaxConnectCalc
      @param ds
   */  
export interface ChangeTaxConnectCalc_input{
      /**  The proposed TaxConnectCalc value.  */  
   proposedTaxConnectCalc:boolean,
   ds:Erp_Tablesets_SalesTaxTableset[],
}

export interface ChangeTaxConnectCalc_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SalesTaxTableset[],
}
}

   /** Required : 
      @param proposedTiming
      @param ds
   */  
export interface ChangeTiming_input{
      /**  The proposed Timing.  */  
   proposedTiming:number,
   ds:Erp_Tablesets_SalesTaxTableset[],
}

export interface ChangeTiming_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SalesTaxTableset[],
}
}

   /** Required : 
      @param newSAFTCode
      @param ds
   */  
export interface CheckPLSAFTCodeAndDescUpdate_input{
   newSAFTCode:string,
   ds:Erp_Tablesets_SalesTaxTableset[],
}

export interface CheckPLSAFTCodeAndDescUpdate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SalesTaxTableset[],
}
}

   /** Required : 
      @param code
   */  
export interface CheckPLSAFTCode_input{
      /**  SAF-T Code  */  
   code:string,
}

export interface CheckPLSAFTCode_output{
}

   /** Required : 
      @param ds
      @param taxCode
      @param rateCode
      @param effectiveFrom
   */  
export interface CopyTaxBoxEffFromLastEffRate_input{
   ds:Erp_Tablesets_SalesTaxTableset[],
   taxCode:string,
   rateCode:string,
   effectiveFrom:string,
}

export interface CopyTaxBoxEffFromLastEffRate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SalesTaxTableset[],
}
}

   /** Required : 
      @param ds
      @param taxCode
      @param rateCode
      @param effectiveFrom
   */  
export interface CopyTaxBoxFromRatesTaxBox_input{
   ds:Erp_Tablesets_SalesTaxTableset[],
   taxCode:string,
   rateCode:string,
   effectiveFrom:string,
}

export interface CopyTaxBoxFromRatesTaxBox_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SalesTaxTableset[],
}
}

   /** Required : 
      @param taxCode
   */  
export interface DeleteByID_input{
   taxCode:string,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param taxCode
      @param rateCode
      @param effectiveFrom
   */  
export interface DisableCopyTaxBoxFromLastEffRate_input{
   taxCode:string,
   rateCode:string,
   effectiveFrom:string,
}

export interface DisableCopyTaxBoxFromLastEffRate_output{
   returnObj:boolean,
}

   /** Required : 
      @param taxCode
      @param rateCode
      @param effectiveFrom
   */  
export interface DisableCopyTaxBoxFromRates_input{
   taxCode:string,
   rateCode:string,
   effectiveFrom:string,
}

export interface DisableCopyTaxBoxFromRates_output{
   returnObj:boolean,
}

export interface Erp_Tablesets_EffRateEntityGLCRow{
      /**  Company Identifier.  */  
   Company:string,
      /**   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  */  
   RelatedToFile:string,
      /**  Major component of the foreign key of the related master record. For example: For a "Part"  control this field would contain the related Part Number,  for a "Customer"  it contains the Customer.CustNum.  */  
   Key1:string,
      /**   2nd component of the foreign key to the related master record.
The usage of this field is dependent on the type of record.  */  
   Key2:string,
      /**   3rd component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key3:string,
      /**   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key4:string,
      /**   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key5:string,
      /**   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key6:string,
      /**  Identifier of the GL Control Type.  */  
   GLControlType:string,
      /**  GL Control Identifier.  */  
   GLControlCode:string,
      /**  Identifies the entity.  Reference only.  Used for integrity validation when deleting a GLCTEntity record.  */  
   BusinessEntity:string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   ExtCompanyID:string,
      /**  Flag to indicate the account in this record is for an external company.  */  
   IsExternalCompany:boolean,
      /**  Marks this EntityGLC as global, available to be sent out to other companies.  */  
   GlobalEntityGLC:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   TaxCode:string,
   RateCode:string,
   EffectiveFrom:string,
   BitFlag:number,
   GLCntrlDescription:string,
   GLCntrlTypeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_EntityGLCRow{
      /**  Company Identifier.  */  
   Company:string,
      /**   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  */  
   RelatedToFile:string,
      /**  Major component of the foreign key of the related master record. For example: For a "Part"  control this field would contain the related Part Number,  for a "Customer"  it contains the Customer.CustNum.  */  
   Key1:string,
      /**   2nd component of the foreign key to the related master record.
The usage of this field is dependent on the type of record.  */  
   Key2:string,
      /**   3rd component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key3:string,
      /**   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key4:string,
      /**   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key5:string,
      /**   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key6:string,
      /**  Identifier of the GL Control Type.  */  
   GLControlType:string,
      /**  GL Control Identifier.  */  
   GLControlCode:string,
      /**  Identifies the entity.  Reference only.  Used for integrity validation when deleting a GLCTEntity record.  */  
   BusinessEntity:string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   ExtCompanyID:string,
      /**  Flag to indicate the account in this record is for an external company.  */  
   IsExternalCompany:boolean,
      /**  Marks this EntityGLC as global, available to be sent out to other companies.  */  
   GlobalEntityGLC:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  BankAcctID of the related BankAcct record.  */  
   BankAcctID:string,
   BankFeeID:string,
      /**  CallCode of the related FSCallCd record.  */  
   CallCode:string,
   ChargeCode:string,
      /**  ClassCode of the related FAClass record.  */  
   ClassCode:string,
      /**  ClassID.  This can be ClassID of PartClass, PRClsDed, or PRClsTax  */  
   ClassID:string,
      /**  ContractCode of the related FSContCd record.  */  
   ContractCode:string,
      /**  CurrencyCode of the related Currency record.  */  
   CurrencyCode:string,
      /**  CustNum of the related Customer record  */  
   CustNum:number,
      /**  DeductionID of PRClsDed or PRDeduct.  */  
   DeductionID:string,
      /**  EmpID of the related PREmpMas record.  */  
   EmpID:string,
      /**  ExpenseCode of PayTLbr, LabExpCd  */  
   ExpenseCode:string,
      /**  ExtSystemID of ExtCompany table  */  
   ExtSystemID:string,
      /**  FromPlant value of the related PlntTranDef record.  */  
   FromPlant:string,
      /**  GroupCode of the related FAGroup record.  */  
   GroupCode:string,
   GroupID:string,
   HeadNum:number,
   InvoiceNum:string,
      /**  JCDept of the related JCDept record.  */  
   JCDept:string,
      /**  MiscCode of the related MiscChrg or PurMisc record.  */  
   MiscCode:string,
      /**  PartNum of the related Part record.  */  
   PartNum:string,
      /**  PayTypeID of PayType  */  
   PayTypeID:string,
   PerConName:string,
      /**  PI Status  */  
   PIStatus:string,
      /**  Plant of the related PlantConfCtrl record.  */  
   Plant:string,
      /**  ProdCode of the related ProdGrup record.  */  
   ProdCode:string,
      /**  ProjectID of the related Project record.  */  
   ProjectID:string,
      /**  PurchCode of the related GLPurch record.  */  
   PurchCode:string,
      /**  RateCode of the related GLRate record.  */  
   RateCode:string,
      /**  ReasonCode of the related Reason record.  */  
   ReasonCode:string,
      /**  ReasonType of the related Reason record.  */  
   ReasonType:string,
      /**  SalesCatID of the related SalesCat record.  */  
   SalesCatID:string,
      /**  Shift value of the related JCShift record.  */  
   Shift:number,
      /**  TaxCode of the related SalesTax record.  */  
   TaxCode:string,
      /**  TaxTblID of PRTaxMas or PRClsTax.  */  
   TaxTblID:string,
      /**  ToPlant value of the related PlntTranDef record.  */  
   ToPlant:string,
      /**  TransferMethod of ExtCompany table  */  
   TransferMethod:string,
      /**  Type ID  */  
   TypeID:string,
      /**  VendorNum of the related Vendor record.  */  
   VendorNum:number,
      /**  WarehouseCode of the related Warehse record.  */  
   WarehouseCode:string,
   ExpenseTypeCode:string,
   IsFiltered:boolean,
   OprTypeCode:string,
   CashDeskID:string,
   TIN:string,
   ReclassCodeID:string,
   BitFlag:number,
   GLCntrlDescription:string,
   GLCntrlTypeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_LangDescRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Name of table that this data is related  */  
   TableName:string,
      /**  Language ID  */  
   LangNameID:string,
      /**  Contains values that represent the key1 to the foreign record that this record is related.  */  
   Key1:string,
      /**  key2  of  the foreign record  */  
   Key2:string,
      /**  key3 of the foreign record  */  
   Key3:string,
      /**  Language Description  */  
   Description:string,
      /**  Marks this LangDesc as global, available to be sent out to other companies.  */  
   GlobalLangDesc:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   LangNameIDDescription:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PLSAFTCodeRow{
      /**  Company  */  
   Company:string,
      /**  RateCode  */  
   RateCode:string,
      /**  TaxCode  */  
   TaxCode:string,
      /**  SAFTCode  */  
   SAFTCode:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   CodeDesc:string,
   LongDesc:string,
   TempSAFTCode:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SalesTRCRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   TaxCode:string,
      /**  Rate Code  */  
   RateCode:string,
      /**  Description  */  
   Description:string,
      /**  Default Rate  */  
   DefaultRate:boolean,
      /**  Legal Text code  */  
   TextCode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  AGAFIPCode  */  
   AGAFIPCode:string,
      /**  AGFEAFIPCode  */  
   AGFEAFIPCode:string,
      /**  AGPurchaseColNumber  */  
   AGPurchaseColNumber:number,
      /**  AGSalesColNumber  */  
   AGSalesColNumber:number,
      /**  Intracom Code (CSF Belgium)  */  
   BEIntracomCode:string,
      /**  JPConsumptionTax  */  
   JPConsumptionTax:boolean,
      /**  PLSAFTCode  */  
   PLSAFTCode:string,
      /**  CODIANCode  */  
   CODIANCode:string,
      /**  UNCL5305  */  
   ExternalTaxCategory:string,
      /**  Indicate if is tring to be deleted from SalesTax  */  
   FatherDeleted:boolean,
   BitFlag:number,
   TaxTextDescription:string,
   XbSystELIEinvoice:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SalesTaxListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   TaxCode:string,
      /**  Full description for a  Sales Tax master.  */  
   Description:string,
      /**  Indicates if the tax calculations are to be performed manually.  This field is used as a default for the InvcTax.Manual field.  When this field is set in the InvcTax record the InvcTax.Reportable, InvcTax.TaxableAmt, and InvcTax.TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations automatically.  */  
   Manual:boolean,
      /**  Indicates if set to Yes that any decimal values of a penny/cent should be rounded down rather than rounded to nearest penny/cent.  */  
   RoundDown:boolean,
      /**  When checked the sales tax code will apply to advanced billing invoices, and will only apply to additional sums on final invoices.  */  
   Advanced:boolean,
      /**  Indicates whether taxes related to this Sales Tax ID are calculated via Epicor Tax Connect interface. Default is No.  */  
   TaxConnectCalc:boolean,
      /**  If this SalesTax id is used by TaxConnect, this is a string containing the data required to uniquely identify a specific taxing jurisdiction using the tax connect system data. It will be used to generate the ETCHash field. If multiple fields from the tax connect system are required to generate a unique key, they should be concatenated, separated by ?:?. For Avalara it will be the StateJurisCode+ ?:? + TaxDetail JurisCode + ?:? + TaxDetail JurisName returned by the GetTax function for each tax amount. Default is null.  */  
   ETCJurisKey:string,
      /**  If this SalesTax id is used by TaxConnect, this is the hash field to be used to cross reference the key fields provided by the tax connect service (stored in ETCJurisKey)  with the Epicor SalesTax id of this record in order to obtain the correct tax accrual GLs for the transaction. Default is null.  */  
   ETCHash:number,
      /**  Collection Type  */  
   CollectionType:number,
      /**  Timing of when to report taxes (default)  */  
   Timing:number,
      /**  Algorithm  */  
   Algorithm:string,
      /**  Discount Types, none, payment discount affect tax, terms discount affect tax  */  
   DiscountType:number,
      /**  Tax Jurisdiction  */  
   TaxJurisCode:string,
      /**  Tax Report Category  */  
   RptCatCode:string,
      /**  Legal Text Code  */  
   TextCode:string,
      /**  In Price  */  
   InPrice:boolean,
      /**  Tax Certificate Numbering method  */  
   LglNumType:number,
      /**  Legal Number Sequence  */  
   LglNumSeq:number,
      /**  Reverse Tax Report Category  */  
   RevRptCatCode:string,
      /**  Intra-EU Service  */  
   ServiceTaxPoint:boolean,
      /**  Sales List Type Indicator  */  
   Direct:string,
      /**  Sales List Type Indicator  */  
   Triangulation:string,
      /**  Marks this SalesTax as global, available to be sent out to other companies.  */  
   GlobalSalesTax:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Invoice Type: 0-No Vat Reporting, 1-Tax Invoice, 2-Duty-Free Invoice  */  
   InvoiceType:string,
      /**  Invoicing Method: 0-No VAT Reporting, 1-Paper Invoice, 2-eInvoice, 3-No Invoice  */  
   InvMethod:string,
      /**  Customer Type: 0-No VAT Reporting, 1-Company Sales, 2-Personal Sales  */  
   CustType:string,
      /**  Revenue Type: 0-No VAT Reporting, 1-Trading Revenue, 2-Non-Trading Revenue  */  
   RevType:string,
      /**  Issue Type: 0-No VAT Reporting, 1-Normal Invoice, 2-Issued by Supplier  */  
   IssueType:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Parent Tax Id  */  
   ParentJurisdiction:string,
      /**  Flag to indicate if Reverse Charge should be enabled.  */  
   EnableRevCharge:boolean,
      /**  Flag to indicate if Tax Box maintenance should be allowed.  */  
   EnableTaxBox:boolean,
      /**  Description of the record, translated in the selected language  */  
   mtlDescription:string,
      /**  Name of the selected language of Description  */  
   mtlLangDesc:string,
      /**  ID of the selected language  */  
   mtlLangId:string,
      /**  Description  */  
   TaxAlgrmDescription:string,
      /**  Description  */  
   TaxJurisDescription:string,
      /**  Description  */  
   TaxRptCatDescription:string,
      /**  Description  */  
   TaxTextDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SalesTaxListTableset{
   SalesTaxList:Erp_Tablesets_SalesTaxListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_SalesTaxRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   TaxCode:string,
      /**  Full description for a  Sales Tax master.  */  
   Description:string,
      /**  Indicates if the tax calculations are to be performed manually.  This field is used as a default for the InvcTax.Manual field.  When this field is set in the InvcTax record the InvcTax.Reportable, InvcTax.TaxableAmt, and InvcTax.TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations automatically.  */  
   Manual:boolean,
      /**  Indicates if set to Yes that any decimal values of a penny/cent should be rounded down rather than rounded to nearest penny/cent.  */  
   RoundDown:boolean,
      /**  When checked the sales tax code will apply to advanced billing invoices, and will only apply to additional sums on final invoices.  */  
   Advanced:boolean,
      /**  Indicates whether taxes related to this Sales Tax ID are calculated via Epicor Tax Connect interface. Default is No.  */  
   TaxConnectCalc:boolean,
      /**  If this SalesTax id is used by TaxConnect, this is a string containing the data required to uniquely identify a specific taxing jurisdiction using the tax connect system data. It will be used to generate the ETCHash field. If multiple fields from the tax connect system are required to generate a unique key, they should be concatenated, separated by ?:?. For Avalara it will be the StateJurisCode+ ?:? + TaxDetail JurisCode + ?:? + TaxDetail JurisName returned by the GetTax function for each tax amount. Default is null.  */  
   ETCJurisKey:string,
      /**  If this SalesTax id is used by TaxConnect, this is the hash field to be used to cross reference the key fields provided by the tax connect service (stored in ETCJurisKey)  with the Epicor SalesTax id of this record in order to obtain the correct tax accrual GLs for the transaction. Default is null.  */  
   ETCHash:number,
      /**  Collection Type  */  
   CollectionType:number,
      /**  Timing of when to report taxes (default)  */  
   Timing:number,
      /**  Algorithm  */  
   Algorithm:string,
      /**  Discount Types, none, payment discount affect tax, terms discount affect tax  */  
   DiscountType:number,
      /**  Tax Jurisdiction  */  
   TaxJurisCode:string,
      /**  Tax Report Category  */  
   RptCatCode:string,
      /**  Legal Text Code  */  
   TextCode:string,
      /**  In Price  */  
   InPrice:boolean,
      /**  Tax Certificate Numbering method  */  
   LglNumType:number,
      /**  Legal Number Sequence  */  
   LglNumSeq:number,
      /**  Reverse Tax Report Category  */  
   RevRptCatCode:string,
      /**  Intra-EU Service  */  
   ServiceTaxPoint:boolean,
      /**  Sales List Type Indicator  */  
   Direct:string,
      /**  Sales List Type Indicator  */  
   Triangulation:string,
      /**  Marks this SalesTax as global, available to be sent out to other companies.  */  
   GlobalSalesTax:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Invoice Type: 0-No Vat Reporting, 1-Tax Invoice, 2-Duty-Free Invoice  */  
   InvoiceType:string,
      /**  Invoicing Method: 0-No VAT Reporting, 1-Paper Invoice, 2-eInvoice, 3-No Invoice  */  
   InvMethod:string,
      /**  Customer Type: 0-No VAT Reporting, 1-Company Sales, 2-Personal Sales  */  
   CustType:string,
      /**  Revenue Type: 0-No VAT Reporting, 1-Trading Revenue, 2-Non-Trading Revenue  */  
   RevType:string,
      /**  Issue Type: 0-No VAT Reporting, 1-Normal Invoice, 2-Issued by Supplier  */  
   IssueType:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  INIsCST  */  
   INIsCST:boolean,
      /**  AGAFIPCode  */  
   AGAFIPCode:string,
      /**  AGAFIPTaxRegCode  */  
   AGAFIPTaxRegCode:string,
      /**  AGAFIPTaxRegDesc  */  
   AGAFIPTaxRegDesc:string,
      /**  AGMinimumByTax  */  
   AGMinimumByTax:boolean,
      /**  AGTaxableAmtType  */  
   AGTaxableAmtType:string,
      /**  AGWHHeader  */  
   AGWHHeader:string,
      /**  IndirectTaxType  */  
   IndirectTaxType:string,
      /**  Mexico Localizaion field to store TaxType Category for Mexico  */  
   MXTaxCategory:string,
      /**  NOTaxCategory  */  
   NOTaxCategory:string,
      /**  PETranDocTypeID  */  
   PETranDocTypeID:string,
      /**  PETaxOriginType  */  
   PETaxOriginType:string,
      /**  MXSATCode  */  
   MXSATCode:string,
      /**  PE SUNAT Code  */  
   PESUNATCode:string,
      /**  PE SUNAT Name  */  
   PESUNATName:string,
      /**  PE SUNAT Type  */  
   PESUNATType:string,
      /**  PLSAFTCode  */  
   PLSAFTCode:string,
      /**  MXTaxType  */  
   MXTaxType:string,
      /**  MXTypeFactor  */  
   MXTypeFactor:string,
      /**  Determines if the tax type has to be synchronized with Epicor FSA application.  */  
   SendToFSA:boolean,
      /**  Timing of when to report taxes (specific to Deposit Billing and Advanced Billing invoices)  */  
   TimingDepositAdvBilling:number,
      /**  E-Invoice Tax Category  */  
   EInvTaxCategory:string,
      /**  PEISCCalcCode  */  
   PEISCCalcCode:string,
      /**  PEAllowanceChargeReasonCode  */  
   PEAllowanceChargeReasonCode:string,
      /**  Tax category; Country specific, e.g. ‘GST’ for ANZ. UNTDID 5153  */  
   ExternalTaxCategory:string,
   AllowConfirmationTax:boolean,
      /**  Flag to indicate if Reverse Charge should be enabled.  */  
   EnableRevCharge:boolean,
      /**  Flag to indicate if Tax Box maintenance should be allowed.  */  
   EnableTaxBox:boolean,
      /**  Description of the record, translated in the selected language  */  
   mtlDescription:string,
      /**  Name of the selected language of Description  */  
   mtlLangDesc:string,
      /**  ID of the selected language  */  
   mtlLangId:string,
      /**  Parent Tax Id  */  
   ParentJurisdiction:string,
   PEISCCalcCodeDesc:string,
   PESUNATCodeDesc:string,
      /**  Flag to indicate if the tax type is assigned to a tax liability.  */  
   EnableChanges:boolean,
      /**  Peru CSF: Allowance Change Reason Code description  */  
   PEAllowanceChargeReasonDesc:string,
   BitFlag:number,
   CompanySendToFSA:boolean,
   TaxAlgrmDescription:string,
   TaxJurisDescription:string,
   TaxRptCatDescription:string,
   TaxTextDescription:string,
   XbSystELIEinvoice:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SalesTaxTableset{
   SalesTax:Erp_Tablesets_SalesTaxRow[],
   LangDesc:Erp_Tablesets_LangDescRow[],
   SalesTRC:Erp_Tablesets_SalesTRCRow[],
   EntityGLC:Erp_Tablesets_EntityGLCRow[],
   SalesTxc:Erp_Tablesets_SalesTxcRow[],
   TaxBox:Erp_Tablesets_TaxBoxRow[],
   TaxRate:Erp_Tablesets_TaxRateRow[],
   EffRateEntityGLC:Erp_Tablesets_EffRateEntityGLCRow[],
   TaxBoxEffRate:Erp_Tablesets_TaxBoxEffRateRow[],
   TaxGRate:Erp_Tablesets_TaxGRateRow[],
   PLSAFTCode:Erp_Tablesets_PLSAFTCodeRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_SalesTxcRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The TaxCode to which this record is related.  */  
   TaxCode:string,
      /**  The TaxCatID which relates this record to the TaxCat record.  */  
   TaxCatID:string,
      /**  Indicates that sales made of tax category are still reportable to the taxing jurisdiction as gross receipts even thou this category is  not  taxable.  */  
   Reportable:boolean,
      /**  Rate Code  */  
   RateCode:string,
      /**  Exemption Type  */  
   ExemptType:number,
      /**  Exemption Percent  */  
   ExemptPercent:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Tax category description  */  
   TaxCatIDDesc:string,
   BitFlag:number,
   TaxCatIDDescription:string,
   TaxCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_TaxBoxEffRateRow{
      /**  Company  */  
   Company:string,
      /**  TaxCode  */  
   TaxCode:string,
      /**  BoxCode  */  
   BoxCode:string,
      /**  SourceModule  */  
   SourceModule:string,
      /**  AmountType  */  
   AmountType:string,
      /**  ECAcquisitionSeq  */  
   ECAcquisitionSeq:number,
      /**  EffectiveFrom  */  
   EffectiveFrom:string,
      /**  BoxSign  */  
   BoxSign:string,
      /**  RateCode  */  
   RateCode:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  Box Code Description  */  
   BoxCodeDescription:string,
      /**  Flag to indicate if Tax Box maintenance should be allowed.  */  
   EnableTaxBox:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_TaxBoxRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   TaxCode:string,
      /**  Tax Box Code.  */  
   BoxCode:string,
      /**   Indicates the source module of the transaction for this tax box.
Possible values are: "AR" = from AR Invoice;  "AP" = from AP Invoice;  "ARCM" = from AR Credit Memo;  "APDM" = from AP Debit Memo.  */  
   SourceModule:string,
      /**  The Amount type to be stored for this tax box.  The possible values are:  "Tax" = for Tax Amount; "Taxable" = for Taxable Amount.  */  
   AmountType:string,
      /**  Indicates if the tax line associated with this tax box is the Primary or Secondary line. This field corresponds to the ECAcquisitionSeq stored in the APInvTax to indicate the second reversing tax line.  Valid values are: 0 = Primary or Standard tax line;  1 = Secondary or Reversing tax line (only created if ECAcquisition or Reverse Charge apply)  */  
   ECAcquisitionSeq:number,
      /**  Sign for box amount. + means add the taxable/tax amount to the (taxable/tax) box value; - means substract the taxable/tax amount from the (taxable/tax) box value.  */  
   BoxSign:string,
      /**  Rate Code  */  
   RateCode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Flag to indicate if Tax Box maintenance should be allowed.  */  
   EnableTaxBox:boolean,
      /**  Box Code Description  */  
   BoxCodeDescription:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_TaxGRateRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   TaxCode:string,
      /**  Tax Rate Code  */  
   RateCode:string,
      /**  First date tax rate is valid for  */  
   EffectiveFrom:string,
      /**  Minimum amount to apply tax to  */  
   FromAmount:number,
      /**  Tax Percent to use  */  
   TaxPercent:number,
      /**  Fixed Tax Amount to apply  */  
   TaxAmount:number,
      /**  Reverse Charge  */  
   ReverseCharge:boolean,
      /**  Unique Identifier for Legal Text  */  
   TextCode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Flag to indicate if Reverse Charge check box is available to the user  */  
   ReverseAvail:boolean,
   CurrencyCode:string,
   BitFlag:number,
   TaxTextDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_TaxRateRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   TaxCode:string,
      /**  Rate Code  */  
   RateCode:string,
      /**  First date tax rate is valid for  */  
   EffectiveFrom:string,
      /**  Percentage, Fixed Value or Graduated Rate  */  
   RateType:number,
      /**  Tax Percent  */  
   TaxPercent:number,
      /**  Fixed Tax Amount  */  
   TaxAmount:number,
      /**  Deduction Percent  */  
   DeductPercent:number,
      /**  Currency Code  */  
   CurrencyCode:string,
      /**  Minimum Amount  */  
   MinAmount:number,
      /**  Maximum Amount  */  
   MaxAmount:number,
      /**  Cent Override Code  */  
   CentCode:string,
      /**  I - Document Level, L - Line Level  */  
   CompMethod:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  PEMinInvAmt  */  
   PEMinInvAmt:number,
      /**  PEMinPayAmt  */  
   PEMinPayAmt:number,
      /**  PEIncTaxAmt  */  
   PEIncTaxAmt:boolean,
      /**  PEWHCurrencyCode  */  
   PEWHCurrencyCode:string,
      /**  Indicates if Deduct percent is not available for changes (always 100%)  */  
   DisableDeduct:boolean,
      /**  PatchField for TaxPercent (using 3 decimals instead of 2)  */  
   DspTaxPercent:number,
      /**  Enable copy Tax Boxes from Last Effective Rate  */  
   EnableCopyTaxBoxFromLEffRate:boolean,
      /**  Enable button copy Tax Boxes from Tax Rate Boxes  */  
   EnableCopyTaxBoxFromRates:boolean,
      /**  Like SalesTax.CollectionType - for technical purpose  */  
   CollectionType:number,
   BitFlag:number,
   CurrencyCurrName:string,
   CurrencyDocumentDesc:string,
   CurrencyCurrDesc:string,
   CurrencyCurrencyID:string,
   CurrencyCurrSymbol:string,
   TaxCentDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtSalesTaxTableset{
   SalesTax:Erp_Tablesets_SalesTaxRow[],
   LangDesc:Erp_Tablesets_LangDescRow[],
   SalesTRC:Erp_Tablesets_SalesTRCRow[],
   EntityGLC:Erp_Tablesets_EntityGLCRow[],
   SalesTxc:Erp_Tablesets_SalesTxcRow[],
   TaxBox:Erp_Tablesets_TaxBoxRow[],
   TaxRate:Erp_Tablesets_TaxRateRow[],
   EffRateEntityGLC:Erp_Tablesets_EffRateEntityGLCRow[],
   TaxBoxEffRate:Erp_Tablesets_TaxBoxEffRateRow[],
   TaxGRate:Erp_Tablesets_TaxGRateRow[],
   PLSAFTCode:Erp_Tablesets_PLSAFTCodeRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param taxCode
   */  
export interface GetByID_input{
   taxCode:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_SalesTaxTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_SalesTaxTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_SalesTaxTableset[],
}

export interface GetCollectionDataForCombo_output{
   returnObj:string,
}

   /** Required : 
      @param collectionType
   */  
export interface GetDiscountTypes_input{
   collectionType:number,
}

export interface GetDiscountTypes_output{
   returnObj:string,
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
   returnObj:Erp_Tablesets_SalesTaxListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param taxCode
      @param rateCode
      @param effectiveFrom
   */  
export interface GetNewEffRateEntityGLCOver_input{
   ds:Erp_Tablesets_SalesTaxTableset[],
      /**  Tax Code of Effective Rate.  */  
   taxCode:string,
      /**  Rate Code of Effective Rate.  */  
   rateCode:string,
      /**  EffectiveFrom date of Effective Rate.  */  
   effectiveFrom:string,
}

export interface GetNewEffRateEntityGLCOver_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SalesTaxTableset[],
}
}

   /** Required : 
      @param ds
      @param relatedToFile
      @param key1
      @param key2
      @param key3
      @param key4
      @param key5
      @param key6
   */  
export interface GetNewEffRateEntityGLC_input{
   ds:Erp_Tablesets_SalesTaxTableset[],
   relatedToFile:string,
   key1:string,
   key2:string,
   key3:string,
   key4:string,
   key5:string,
   key6:string,
}

export interface GetNewEffRateEntityGLC_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SalesTaxTableset[],
}
}

   /** Required : 
      @param ds
      @param relatedToFile
      @param key1
      @param key2
      @param key3
      @param key4
      @param key5
      @param key6
   */  
export interface GetNewEntityGLC_input{
   ds:Erp_Tablesets_SalesTaxTableset[],
   relatedToFile:string,
   key1:string,
   key2:string,
   key3:string,
   key4:string,
   key5:string,
   key6:string,
}

export interface GetNewEntityGLC_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SalesTaxTableset[],
}
}

   /** Required : 
      @param ds
      @param tableName
      @param key1
      @param key2
      @param key3
   */  
export interface GetNewLangDesc_input{
   ds:Erp_Tablesets_SalesTaxTableset[],
   tableName:string,
   key1:string,
   key2:string,
   key3:string,
}

export interface GetNewLangDesc_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SalesTaxTableset[],
}
}

   /** Required : 
      @param ds
      @param rateCode
      @param taxCode
   */  
export interface GetNewPLSAFTCode_input{
   ds:Erp_Tablesets_SalesTaxTableset[],
   rateCode:string,
   taxCode:string,
}

export interface GetNewPLSAFTCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SalesTaxTableset[],
}
}

   /** Required : 
      @param ds
      @param taxCode
   */  
export interface GetNewSalesTRC_input{
   ds:Erp_Tablesets_SalesTaxTableset[],
   taxCode:string,
}

export interface GetNewSalesTRC_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SalesTaxTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewSalesTax_input{
   ds:Erp_Tablesets_SalesTaxTableset[],
}

export interface GetNewSalesTax_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SalesTaxTableset[],
}
}

   /** Required : 
      @param ds
      @param taxCode
      @param rateCode
   */  
export interface GetNewSalesTxc_input{
   ds:Erp_Tablesets_SalesTaxTableset[],
   taxCode:string,
   rateCode:string,
}

export interface GetNewSalesTxc_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SalesTaxTableset[],
}
}

   /** Required : 
      @param ds
      @param taxCode
      @param rateCode
      @param effectiveFrom
   */  
export interface GetNewTaxBoxEffRateOver_input{
   ds:Erp_Tablesets_SalesTaxTableset[],
   taxCode:string,
   rateCode:string,
   effectiveFrom:string,
}

export interface GetNewTaxBoxEffRateOver_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SalesTaxTableset[],
}
}

   /** Required : 
      @param ds
      @param taxCode
      @param rateCode
      @param boxCode
      @param sourceModule
      @param amountType
      @param ecAcquisitionSeq
   */  
export interface GetNewTaxBoxEffRate_input{
   ds:Erp_Tablesets_SalesTaxTableset[],
   taxCode:string,
   rateCode:string,
   boxCode:string,
   sourceModule:string,
   amountType:string,
   ecAcquisitionSeq:number,
}

export interface GetNewTaxBoxEffRate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SalesTaxTableset[],
}
}

   /** Required : 
      @param ds
      @param taxCode
      @param rateCode
      @param boxCode
      @param sourceModule
      @param amountType
   */  
export interface GetNewTaxBox_input{
   ds:Erp_Tablesets_SalesTaxTableset[],
   taxCode:string,
   rateCode:string,
   boxCode:string,
   sourceModule:string,
   amountType:string,
}

export interface GetNewTaxBox_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SalesTaxTableset[],
}
}

   /** Required : 
      @param ds
      @param taxCode
      @param rateCode
      @param effectiveFrom
   */  
export interface GetNewTaxGRate_input{
   ds:Erp_Tablesets_SalesTaxTableset[],
   taxCode:string,
   rateCode:string,
   effectiveFrom:string,
}

export interface GetNewTaxGRate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SalesTaxTableset[],
}
}

   /** Required : 
      @param ds
      @param taxCode
      @param rateCode
   */  
export interface GetNewTaxRate_input{
   ds:Erp_Tablesets_SalesTaxTableset[],
   taxCode:string,
   rateCode:string,
}

export interface GetNewTaxRate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SalesTaxTableset[],
}
}

export interface GetNumberingValues_output{
   returnObj:string,
}

   /** Required : 
      @param collectionType
   */  
export interface GetRateTypes_input{
      /**  SalesTax.CollectionType  */  
   collectionType:number,
}

export interface GetRateTypes_output{
   returnObj:string,
}

   /** Required : 
      @param whereClauseSalesTax
      @param whereClauseLangDesc
      @param whereClauseSalesTRC
      @param whereClauseEntityGLC
      @param whereClauseSalesTxc
      @param whereClauseTaxBox
      @param whereClauseTaxRate
      @param whereClauseEffRateEntityGLC
      @param whereClauseTaxBoxEffRate
      @param whereClauseTaxGRate
      @param whereClausePLSAFTCode
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseSalesTax:string,
   whereClauseLangDesc:string,
   whereClauseSalesTRC:string,
   whereClauseEntityGLC:string,
   whereClauseSalesTxc:string,
   whereClauseTaxBox:string,
   whereClauseTaxRate:string,
   whereClauseEffRateEntityGLC:string,
   whereClauseTaxBoxEffRate:string,
   whereClauseTaxGRate:string,
   whereClausePLSAFTCode:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_SalesTaxTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param collectionType
   */  
export interface GetTimingDataForCombo_input{
   collectionType:number,
}

export interface GetTimingDataForCombo_output{
   returnObj:string,
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
      @param code
      @param rateCode
      @param taxCode
      @param ds
   */  
export interface LookupPLSAFTCode_input{
   code:string,
   rateCode:string,
   taxCode:string,
   ds:Erp_Tablesets_SalesTaxTableset[],
}

export interface LookupPLSAFTCode_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SalesTaxTableset[],
}
}

   /** Required : 
      @param value
      @param ds
   */  
export interface PEChangeType_input{
      /**  value  */  
   value:string,
   ds:Erp_Tablesets_SalesTaxTableset[],
}

export interface PEChangeType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SalesTaxTableset[],
}
}

   /** Required : 
      @param codeType
      @param ds
   */  
export interface PEChangeUDCode_input{
      /**  User code  */  
   codeType:string,
   ds:Erp_Tablesets_SalesTaxTableset[],
}

export interface PEChangeUDCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SalesTaxTableset[],
}
}

   /** Required : 
      @param rateCode
      @param taxCode
   */  
export interface RemovePLSAFTCode_input{
   rateCode:string,
   taxCode:string,
}

export interface RemovePLSAFTCode_output{
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtSalesTaxTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtSalesTaxTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface UpdatePLSAFTCode_input{
   ds:Erp_Tablesets_SalesTaxTableset[],
}

export interface UpdatePLSAFTCode_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SalesTaxTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_SalesTaxTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SalesTaxTableset[],
}
}

   /** Required : 
      @param sTaxCode
      @param sRateCode
      @param dEffectiveDate
   */  
export interface ValidateEffectiveDate_input{
      /**  Tax code  */  
   sTaxCode:string,
      /**  Rate Code  */  
   sRateCode:string,
      /**  Returns VendorNum as a character  */  
   dEffectiveDate:string,
}

export interface ValidateEffectiveDate_output{
}

