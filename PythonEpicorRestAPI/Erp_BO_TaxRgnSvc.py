import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.TaxRgnSvc
# Description: The Tax Region service.
# Version: v1



#########################################################################
# OData methods:
#########################################################################
async def getServiceDocument(epicorHeaders = None):
   """  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => application/json
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxRgnSvc/",headers=creds) as resp:
           return await resp.json()

async def get_metadata(epicorHeaders = None):
   """  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: Returns metadata document => content
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxRgnSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_TaxRgns(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get TaxRgns items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TaxRgns
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxRgnRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxRgnSvc/TaxRgns",headers=creds) as resp:
           return await resp.json()

async def post_TaxRgns(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TaxRgns
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TaxRgnRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TaxRgnRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxRgnSvc/TaxRgns", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_TaxRgns_Company_TaxRegionCode(Company, TaxRegionCode, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TaxRgn item
   Description: Calls GetByID to retrieve the TaxRgn item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxRgn
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxRegionCode: Desc: TaxRegionCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxRgnRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxRgnSvc/TaxRgns(" + Company + "," + TaxRegionCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_TaxRgns_Company_TaxRegionCode(Company, TaxRegionCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update TaxRgn for the service
   Description: Calls UpdateExt to update TaxRgn. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TaxRgn
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxRegionCode: Desc: TaxRegionCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TaxRgnRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.TaxRgnSvc/TaxRgns(" + Company + "," + TaxRegionCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_TaxRgns_Company_TaxRegionCode(Company, TaxRegionCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete TaxRgn item
   Description: Call UpdateExt to delete TaxRgn item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TaxRgn
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxRegionCode: Desc: TaxRegionCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.TaxRgnSvc/TaxRgns(" + Company + "," + TaxRegionCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_TaxRgns_Company_TaxRegionCode_TaxRgnSalesTaxes(Company, TaxRegionCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get TaxRgnSalesTaxes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TaxRgnSalesTaxes1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxRegionCode: Desc: TaxRegionCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxRgnSalesTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxRgnSvc/TaxRgns(" + Company + "," + TaxRegionCode + ")/TaxRgnSalesTaxes",headers=creds) as resp:
           return await resp.json()

async def get_TaxRgns_Company_TaxRegionCode_TaxRgnSalesTaxes_Company_TaxRegionCode_TaxCode(Company, TaxRegionCode, TaxCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TaxRgnSalesTax item
   Description: Calls GetByID to retrieve the TaxRgnSalesTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxRgnSalesTax1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxRegionCode: Desc: TaxRegionCode   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxRgnSalesTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxRgnSvc/TaxRgns(" + Company + "," + TaxRegionCode + ")/TaxRgnSalesTaxes(" + Company + "," + TaxRegionCode + "," + TaxCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_TaxRgnSalesTaxes(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get TaxRgnSalesTaxes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TaxRgnSalesTaxes
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxRgnSalesTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxRgnSvc/TaxRgnSalesTaxes",headers=creds) as resp:
           return await resp.json()

async def post_TaxRgnSalesTaxes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TaxRgnSalesTaxes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TaxRgnSalesTaxRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TaxRgnSalesTaxRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxRgnSvc/TaxRgnSalesTaxes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_TaxRgnSalesTaxes_Company_TaxRegionCode_TaxCode(Company, TaxRegionCode, TaxCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TaxRgnSalesTax item
   Description: Calls GetByID to retrieve the TaxRgnSalesTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxRgnSalesTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxRegionCode: Desc: TaxRegionCode   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxRgnSalesTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxRgnSvc/TaxRgnSalesTaxes(" + Company + "," + TaxRegionCode + "," + TaxCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_TaxRgnSalesTaxes_Company_TaxRegionCode_TaxCode(Company, TaxRegionCode, TaxCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update TaxRgnSalesTax for the service
   Description: Calls UpdateExt to update TaxRgnSalesTax. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TaxRgnSalesTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxRegionCode: Desc: TaxRegionCode   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TaxRgnSalesTaxRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.TaxRgnSvc/TaxRgnSalesTaxes(" + Company + "," + TaxRegionCode + "," + TaxCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_TaxRgnSalesTaxes_Company_TaxRegionCode_TaxCode(Company, TaxRegionCode, TaxCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete TaxRgnSalesTax item
   Description: Call UpdateExt to delete TaxRgnSalesTax item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TaxRgnSalesTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxRegionCode: Desc: TaxRegionCode   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.TaxRgnSvc/TaxRgnSalesTaxes(" + Company + "," + TaxRegionCode + "," + TaxCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_List(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxRgnListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxRgnSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseTaxRgn, whereClauseTaxRgnSalesTax, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseTaxRgn=" + whereClauseTaxRgn
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseTaxRgnSalesTax=" + whereClauseTaxRgnSalesTax
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxRgnSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(taxRegionCode, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "taxRegionCode=" + taxRegionCode

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxRgnSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetList(whereClause, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      :param whereClause: Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      :param pageSize: Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      :param absolutePage: Desc: Page of rows to return.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClause=" + whereClause
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxRgnSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetListRegularReturn(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListRegularReturn
   Description: Method to return/non-return tax Liabilities list for search
(Turkish Localization)
   OperationID: GetListRegularReturn
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListRegularReturn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListRegularReturn_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxRgnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MoveTaxOnePosition(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MoveTaxOnePosition
   Description: This method moves the TaxRgn/TaxRgnSalesTax Tax Type Up/Down one position in the
grid and returns the whole updated datatable.
   OperationID: MoveTaxOnePosition
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MoveTaxOnePosition_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MoveTaxOnePosition_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxRgnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeExemptType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeExemptType
   Description: This method validates SalesTaxCode and populates description.
   OperationID: OnChangeExemptType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeExemptType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeExemptType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxRgnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeInPrice(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeInPrice
   Description: This method changes the value of IncludeInAP when InPrice is true.
   OperationID: OnChangeInPrice
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeInPrice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeInPrice_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxRgnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeSalesTaxCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeSalesTaxCode
   Description: This method validates SalesTaxCode and populates description.
   OperationID: OnChangeSalesTaxCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeSalesTaxCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSalesTaxCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxRgnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeTaxMethod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeTaxMethod
   Description: This method validates SalesTaxCode and populates description.
   OperationID: OnChangeTaxMethod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeTaxMethod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTaxMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxRgnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeUseInAR(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeUseInAR
   Description: This method validates SalesTaxCode and populates description.
   OperationID: OnChangeUseInAR
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeUseInAR_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeUseInAR_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxRgnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateExemptPercent(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateExemptPercent
   Description: This method validates Exempt percent to be assign between 0 and 100.
   OperationID: ValidateExemptPercent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateExemptPercent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateExemptPercent_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxRgnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeINDefault(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeINDefault
   Description: This method provides that INDefault flag would be set only one record with current TLT.
   OperationID: OnChangeINDefault
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeINDefault_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeINDefault_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxRgnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewTaxRgn(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewTaxRgn
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTaxRgn
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTaxRgn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTaxRgn_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxRgnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewTaxRgnSalesTax(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewTaxRgnSalesTax
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTaxRgnSalesTax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTaxRgnSalesTax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTaxRgnSalesTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxRgnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxRgnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowID(id, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "id=" + id

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxRgnSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowIDs(ids, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ids=" + ids

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxRgnSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_Update(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
   OperationID: Update
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxRgnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateExt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxRgnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxRgnListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TaxRgnListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxRgnRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TaxRgnRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxRgnSalesTaxRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TaxRgnSalesTaxRow] = obj["value"]
      pass

class Erp_Tablesets_TaxRgnListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Unique identifier of the Tax Region assigned by the user.  """  
      self.Description:str = obj["Description"]
      """  Full description for the Tax Region.  """  
      self.InEC:bool = obj["InEC"]
      """  Tax Region is in the European Community.  """  
      self.TaxConnectCalc:bool = obj["TaxConnectCalc"]
      """  If true, transactions using this tax region will use the tax connect system to calculate taxes. If false, taxes will be calculated using the standard calc methods.  """  
      self.UseInAP:bool = obj["UseInAP"]
      """  Use Tax Liability in AP  """  
      self.UseInAR:bool = obj["UseInAR"]
      """  Use Tax Liability in AR  """  
      self.EUThirdParty:bool = obj["EUThirdParty"]
      """  EU VAT third party flag  """  
      self.InPrice:bool = obj["InPrice"]
      """  Indicates that the tax is included in the unit price  """  
      self.GlobalTaxRgn:bool = obj["GlobalTaxRgn"]
      """  Marks this TaxRgn as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RetTaxRgnCode:str = obj["RetTaxRgnCode"]
      """  RetTaxRgnCode  """  
      self.IsReturn:bool = obj["IsReturn"]
      """  IsReturn  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaxRgnRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Unique identifier of the Tax Region assigned by the user.  """  
      self.Description:str = obj["Description"]
      """  Full description for the Tax Region.  """  
      self.InEC:bool = obj["InEC"]
      """  Tax Region is in the European Community.  """  
      self.TaxConnectCalc:bool = obj["TaxConnectCalc"]
      """  If true, transactions using this tax region will use the tax connect system to calculate taxes. If false, taxes will be calculated using the standard calc methods.  """  
      self.UseInAP:bool = obj["UseInAP"]
      """  Use Tax Liability in AP  """  
      self.UseInAR:bool = obj["UseInAR"]
      """  Use Tax Liability in AR  """  
      self.EUThirdParty:bool = obj["EUThirdParty"]
      """  EU VAT third party flag  """  
      self.InPrice:bool = obj["InPrice"]
      """  Indicates that the tax is included in the unit price  """  
      self.GlobalTaxRgn:bool = obj["GlobalTaxRgn"]
      """  Marks this TaxRgn as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.INTaxLiabilityType:str = obj["INTaxLiabilityType"]
      """  INTaxLiabilityType  """  
      self.INDefault:bool = obj["INDefault"]
      """  INDefault  """  
      self.RetTaxRgnCode:str = obj["RetTaxRgnCode"]
      """  RetTaxRgnCode  """  
      self.NonTaxableDep:bool = obj["NonTaxableDep"]
      """  NonTaxableDep  """  
      self.IsReturn:bool = obj["IsReturn"]
      """  IsReturn  """  
      self.JPConsumptionTaxType:str = obj["JPConsumptionTaxType"]
      """  Japan Consumption Tax Type  """  
      self.CalcTaxIC:bool = obj["CalcTaxIC"]
      """  If enabled the system will recalculate taxes for Intercompany PO’s AP Invoices, if not the taxes will be the same as those of the AR Shipment Invoice from the sending company.  """  
      self.COSpecialTaxRegime:str = obj["COSpecialTaxRegime"]
      """  COSpecialTaxRegime  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaxRgnSalesTaxRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  TaxRgn.TaxRegionCode value that the taxes are applicable to.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  SalesTax.TaxCode value of the sales tax being assigned to the Tax Region.  """  
      self.TaxMethod:str = obj["TaxMethod"]
      """  Tax calculation per line or invoice.  It can be "L" = per line or "I" = per invoice.  Default is "L".  """  
      self.ExemptType:int = obj["ExemptType"]
      """  Exemption Type  """  
      self.ExemptPercent:int = obj["ExemptPercent"]
      """  Exemption Percent  """  
      self.TaxNum:int = obj["TaxNum"]
      """  Order in which to apply taxes  """  
      self.GlobalTaxRgnSalesTax:bool = obj["GlobalTaxRgnSalesTax"]
      """  Marks this TaxRgnSalesTax as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.InPrice:bool = obj["InPrice"]
      """  Indicates that this tax is included in the unit price. Copied from TaxRgn.InPrice  """  
      self.BitFlag:int = obj["BitFlag"]
      self.TaxCodeDescription:str = obj["TaxCodeDescription"]
      self.TaxRegionCodeDescription:str = obj["TaxRegionCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   taxRegionCode
   """  
   def __init__(self, obj):
      self.taxRegionCode:str = obj["taxRegionCode"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_TaxRgnListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Unique identifier of the Tax Region assigned by the user.  """  
      self.Description:str = obj["Description"]
      """  Full description for the Tax Region.  """  
      self.InEC:bool = obj["InEC"]
      """  Tax Region is in the European Community.  """  
      self.TaxConnectCalc:bool = obj["TaxConnectCalc"]
      """  If true, transactions using this tax region will use the tax connect system to calculate taxes. If false, taxes will be calculated using the standard calc methods.  """  
      self.UseInAP:bool = obj["UseInAP"]
      """  Use Tax Liability in AP  """  
      self.UseInAR:bool = obj["UseInAR"]
      """  Use Tax Liability in AR  """  
      self.EUThirdParty:bool = obj["EUThirdParty"]
      """  EU VAT third party flag  """  
      self.InPrice:bool = obj["InPrice"]
      """  Indicates that the tax is included in the unit price  """  
      self.GlobalTaxRgn:bool = obj["GlobalTaxRgn"]
      """  Marks this TaxRgn as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RetTaxRgnCode:str = obj["RetTaxRgnCode"]
      """  RetTaxRgnCode  """  
      self.IsReturn:bool = obj["IsReturn"]
      """  IsReturn  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaxRgnListTableset:
   def __init__(self, obj):
      self.TaxRgnList:list[Erp_Tablesets_TaxRgnListRow] = obj["TaxRgnList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_TaxRgnRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Unique identifier of the Tax Region assigned by the user.  """  
      self.Description:str = obj["Description"]
      """  Full description for the Tax Region.  """  
      self.InEC:bool = obj["InEC"]
      """  Tax Region is in the European Community.  """  
      self.TaxConnectCalc:bool = obj["TaxConnectCalc"]
      """  If true, transactions using this tax region will use the tax connect system to calculate taxes. If false, taxes will be calculated using the standard calc methods.  """  
      self.UseInAP:bool = obj["UseInAP"]
      """  Use Tax Liability in AP  """  
      self.UseInAR:bool = obj["UseInAR"]
      """  Use Tax Liability in AR  """  
      self.EUThirdParty:bool = obj["EUThirdParty"]
      """  EU VAT third party flag  """  
      self.InPrice:bool = obj["InPrice"]
      """  Indicates that the tax is included in the unit price  """  
      self.GlobalTaxRgn:bool = obj["GlobalTaxRgn"]
      """  Marks this TaxRgn as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.INTaxLiabilityType:str = obj["INTaxLiabilityType"]
      """  INTaxLiabilityType  """  
      self.INDefault:bool = obj["INDefault"]
      """  INDefault  """  
      self.RetTaxRgnCode:str = obj["RetTaxRgnCode"]
      """  RetTaxRgnCode  """  
      self.NonTaxableDep:bool = obj["NonTaxableDep"]
      """  NonTaxableDep  """  
      self.IsReturn:bool = obj["IsReturn"]
      """  IsReturn  """  
      self.JPConsumptionTaxType:str = obj["JPConsumptionTaxType"]
      """  Japan Consumption Tax Type  """  
      self.CalcTaxIC:bool = obj["CalcTaxIC"]
      """  If enabled the system will recalculate taxes for Intercompany PO’s AP Invoices, if not the taxes will be the same as those of the AR Shipment Invoice from the sending company.  """  
      self.COSpecialTaxRegime:str = obj["COSpecialTaxRegime"]
      """  COSpecialTaxRegime  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaxRgnSalesTaxRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  TaxRgn.TaxRegionCode value that the taxes are applicable to.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  SalesTax.TaxCode value of the sales tax being assigned to the Tax Region.  """  
      self.TaxMethod:str = obj["TaxMethod"]
      """  Tax calculation per line or invoice.  It can be "L" = per line or "I" = per invoice.  Default is "L".  """  
      self.ExemptType:int = obj["ExemptType"]
      """  Exemption Type  """  
      self.ExemptPercent:int = obj["ExemptPercent"]
      """  Exemption Percent  """  
      self.TaxNum:int = obj["TaxNum"]
      """  Order in which to apply taxes  """  
      self.GlobalTaxRgnSalesTax:bool = obj["GlobalTaxRgnSalesTax"]
      """  Marks this TaxRgnSalesTax as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.InPrice:bool = obj["InPrice"]
      """  Indicates that this tax is included in the unit price. Copied from TaxRgn.InPrice  """  
      self.BitFlag:int = obj["BitFlag"]
      self.TaxCodeDescription:str = obj["TaxCodeDescription"]
      self.TaxRegionCodeDescription:str = obj["TaxRegionCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaxRgnTableset:
   def __init__(self, obj):
      self.TaxRgn:list[Erp_Tablesets_TaxRgnRow] = obj["TaxRgn"]
      self.TaxRgnSalesTax:list[Erp_Tablesets_TaxRgnSalesTaxRow] = obj["TaxRgnSalesTax"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtTaxRgnTableset:
   def __init__(self, obj):
      self.TaxRgn:list[Erp_Tablesets_TaxRgnRow] = obj["TaxRgn"]
      self.TaxRgnSalesTax:list[Erp_Tablesets_TaxRgnSalesTaxRow] = obj["TaxRgnSalesTax"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   taxRegionCode
   """  
   def __init__(self, obj):
      self.taxRegionCode:str = obj["taxRegionCode"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TaxRgnTableset] = obj["returnObj"]
      pass

class GetBySysRowID_input:
   """ Required : 
   id
   """  
   def __init__(self, obj):
      self.id:str = obj["id"]
      pass

class GetBySysRowID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TaxRgnTableset] = obj["returnObj"]
      pass

class GetBySysRowIDs_input:
   """ Required : 
   ids
   """  
   def __init__(self, obj):
      self.ids:str = obj["ids"]
      pass

class GetBySysRowIDs_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TaxRgnTableset] = obj["returnObj"]
      pass

class GetListRegularReturn_input:
   """ Required : 
   Module
   Regular
   PageSize
   AbsolutePage
   """  
   def __init__(self, obj):
      self.Module:str = obj["Module"]
      """  Defines the module for which Tax Liabilities are searched (AP/AR)  """  
      self.Regular:bool = obj["Regular"]
      """  Defines if Regular (true) or Return (false) liabilities list should be returned  """  
      self.PageSize:int = obj["PageSize"]
      """  The maximum number of rows to return. Leave as zero for no maximum  """  
      self.AbsolutePage:int = obj["AbsolutePage"]
      """  Page of rows to return  """  
      pass

class GetListRegularReturn_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TaxRgnListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.MorePages:bool = obj["MorePages"]
      pass

      """  output parameters  """  

class GetList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  An expression used to filter the rows. Can be left blank for all rows.  """  
      self.pageSize:int = obj["pageSize"]
      """  The maximum number of rows to return. Leave as zero for no maximum.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Page of rows to return.  """  
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TaxRgnListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewTaxRgnSalesTax_input:
   """ Required : 
   ds
   taxRegionCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaxRgnTableset] = obj["ds"]
      self.taxRegionCode:str = obj["taxRegionCode"]
      pass

class GetNewTaxRgnSalesTax_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaxRgnTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewTaxRgn_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaxRgnTableset] = obj["ds"]
      pass

class GetNewTaxRgn_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaxRgnTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseTaxRgn
   whereClauseTaxRgnSalesTax
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseTaxRgn:str = obj["whereClauseTaxRgn"]
      self.whereClauseTaxRgnSalesTax:str = obj["whereClauseTaxRgnSalesTax"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TaxRgnTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class Ice_BOUpdErrorRow:
   def __init__(self, obj):
      self.TableName:str = obj["TableName"]
      self.ErrorLevel:str = obj["ErrorLevel"]
      self.ErrorType:str = obj["ErrorType"]
      self.ErrorText:str = obj["ErrorText"]
      self.ErrorSysRowID:str = obj["ErrorSysRowID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_BOUpdErrorTableset:
   def __init__(self, obj):
      self.BOUpdError:list[Ice_BOUpdErrorRow] = obj["BOUpdError"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Extensions_ExtensionRow:
   def __init__(self, obj):
      self.ColumnValues:object
      self.RowMod:str = obj["RowMod"]
      self.SysRowID:str = obj["SysRowID"]
      pass

class Ice_Extensions_ExtensionTableColumn:
   def __init__(self, obj):
      self.ColumnName:str = obj["ColumnName"]
      self.ColumnType:str = obj["ColumnType"]
      pass

class Ice_Extensions_ExtensionTableData:
   def __init__(self, obj):
      self.Table:list[Ice_Extensions_ExtensionRow] = obj["Table"]
      self.SystemCode:str = obj["SystemCode"]
      self.TableName:str = obj["TableName"]
      self.Columns:list[Ice_Extensions_ExtensionTableColumn] = obj["Columns"]
      self.PrimaryKeyColumns:str = obj["PrimaryKeyColumns"]
      self.PeerTableSystemCode:str = obj["PeerTableSystemCode"]
      self.PeerTableName:str = obj["PeerTableName"]
      pass

class MoveTaxOnePosition_input:
   """ Required : 
   taxRegionCode
   taxCode
   taxNum
   moveDir
   """  
   def __init__(self, obj):
      self.taxRegionCode:str = obj["taxRegionCode"]
      """  Tax Region Code  """  
      self.taxCode:str = obj["taxCode"]
      """  Tax Code  """  
      self.taxNum:int = obj["taxNum"]
      """  Tax Sequence number of tax type to move  """  
      self.moveDir:str = obj["moveDir"]
      """  Direction to move task, "Up" or "Down"  """  
      pass

class MoveTaxOnePosition_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TaxRgnTableset] = obj["returnObj"]
      pass

class OnChangeExemptType_input:
   """ Required : 
   ds
   iProposedExemptType
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaxRgnTableset] = obj["ds"]
      self.iProposedExemptType:int = obj["iProposedExemptType"]
      """  The proposed Exempt type value  """  
      pass

class OnChangeExemptType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaxRgnTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeINDefault_input:
   """ Required : 
   ds
   iProposedINDefault
   iTaxLiabilityType
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaxRgnTableset] = obj["ds"]
      self.iProposedINDefault:bool = obj["iProposedINDefault"]
      """  The proposed INDefault flag  """  
      self.iTaxLiabilityType:str = obj["iTaxLiabilityType"]
      """  Current TL type  """  
      pass

class OnChangeINDefault_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaxRgnTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeInPrice_input:
   """ Required : 
   ds
   iProposedInPrice
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaxRgnTableset] = obj["ds"]
      self.iProposedInPrice:bool = obj["iProposedInPrice"]
      """  The proposed InPrice flag  """  
      pass

class OnChangeInPrice_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaxRgnTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeSalesTaxCode_input:
   """ Required : 
   ds
   iProposedSalesTaxCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaxRgnTableset] = obj["ds"]
      self.iProposedSalesTaxCode:str = obj["iProposedSalesTaxCode"]
      """  The proposed SalesTaxCode value  """  
      pass

class OnChangeSalesTaxCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaxRgnTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeTaxMethod_input:
   """ Required : 
   ds
   iProposedTaxMethod
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaxRgnTableset] = obj["ds"]
      self.iProposedTaxMethod:str = obj["iProposedTaxMethod"]
      """  The proposed Tax Method value  """  
      pass

class OnChangeTaxMethod_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaxRgnTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeUseInAR_input:
   """ Required : 
   ds
   iProposedUseInAR
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaxRgnTableset] = obj["ds"]
      self.iProposedUseInAR:bool = obj["iProposedUseInAR"]
      """  The proposed UseInAR flag  """  
      pass

class OnChangeUseInAR_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaxRgnTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtTaxRgnTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtTaxRgnTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaxRgnTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaxRgnTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateExemptPercent_input:
   """ Required : 
   ipExemptType
   ipExemptPercent
   """  
   def __init__(self, obj):
      self.ipExemptType:int = obj["ipExemptType"]
      """  Exempt Type  """  
      self.ipExemptPercent:int = obj["ipExemptPercent"]
      """  Exempt Percent  """  
      pass

class ValidateExemptPercent_output:
   def __init__(self, obj):
      pass

