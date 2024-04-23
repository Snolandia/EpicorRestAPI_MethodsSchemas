import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.DashboardMaintSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DashboardMaintSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DashboardMaintSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_DashboardMaints(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DashboardMaints items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DashboardMaints
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.DashboardMaintRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DashboardMaintSvc/DashboardMaints",headers=creds) as resp:
           return await resp.json()

async def post_DashboardMaints(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DashboardMaints
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.DashboardMaintRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.DashboardMaintRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DashboardMaintSvc/DashboardMaints", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DashboardMaints_Company_ProductID_GlbCompany_CGCCode_DefinitionID(Company, ProductID, GlbCompany, CGCCode, DefinitionID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DashboardMaint item
   Description: Calls GetByID to retrieve the DashboardMaint item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DashboardMaint
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProductID: Desc: ProductID   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param CGCCode: Desc: CGCCode   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.DashboardMaintRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DashboardMaintSvc/DashboardMaints(" + Company + "," + ProductID + "," + GlbCompany + "," + CGCCode + "," + DefinitionID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DashboardMaints_Company_ProductID_GlbCompany_CGCCode_DefinitionID(Company, ProductID, GlbCompany, CGCCode, DefinitionID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DashboardMaint for the service
   Description: Calls UpdateExt to update DashboardMaint. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DashboardMaint
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProductID: Desc: ProductID   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param CGCCode: Desc: CGCCode   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.DashboardMaintRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.DashboardMaintSvc/DashboardMaints(" + Company + "," + ProductID + "," + GlbCompany + "," + CGCCode + "," + DefinitionID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DashboardMaints_Company_ProductID_GlbCompany_CGCCode_DefinitionID(Company, ProductID, GlbCompany, CGCCode, DefinitionID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DashboardMaint item
   Description: Call UpdateExt to delete DashboardMaint item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DashboardMaint
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProductID: Desc: ProductID   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param CGCCode: Desc: CGCCode   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.DashboardMaintSvc/DashboardMaints(" + Company + "," + ProductID + "," + GlbCompany + "," + CGCCode + "," + DefinitionID + ")",headers=creds) as resp:
           return await resp.json()

async def get_DashBdBAQs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DashBdBAQs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DashBdBAQs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.DashBdBAQRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DashboardMaintSvc/DashBdBAQs",headers=creds) as resp:
           return await resp.json()

async def post_DashBdBAQs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DashBdBAQs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.DashBdBAQRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.DashBdBAQRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DashboardMaintSvc/DashBdBAQs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DashBdBAQs_Company_ProductID_GlbCompany_CGCCode_DefinitionID_QueryID(Company, ProductID, GlbCompany, CGCCode, DefinitionID, QueryID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DashBdBAQ item
   Description: Calls GetByID to retrieve the DashBdBAQ item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DashBdBAQ
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProductID: Desc: ProductID   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param CGCCode: Desc: CGCCode   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.DashBdBAQRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DashboardMaintSvc/DashBdBAQs(" + Company + "," + ProductID + "," + GlbCompany + "," + CGCCode + "," + DefinitionID + "," + QueryID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DashBdBAQs_Company_ProductID_GlbCompany_CGCCode_DefinitionID_QueryID(Company, ProductID, GlbCompany, CGCCode, DefinitionID, QueryID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DashBdBAQ for the service
   Description: Calls UpdateExt to update DashBdBAQ. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DashBdBAQ
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProductID: Desc: ProductID   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param CGCCode: Desc: CGCCode   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.DashBdBAQRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.DashboardMaintSvc/DashBdBAQs(" + Company + "," + ProductID + "," + GlbCompany + "," + CGCCode + "," + DefinitionID + "," + QueryID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DashBdBAQs_Company_ProductID_GlbCompany_CGCCode_DefinitionID_QueryID(Company, ProductID, GlbCompany, CGCCode, DefinitionID, QueryID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DashBdBAQ item
   Description: Call UpdateExt to delete DashBdBAQ item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DashBdBAQ
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProductID: Desc: ProductID   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param CGCCode: Desc: CGCCode   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.DashboardMaintSvc/DashBdBAQs(" + Company + "," + ProductID + "," + GlbCompany + "," + CGCCode + "," + DefinitionID + "," + QueryID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.DashboardMaintListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DashboardMaintSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseDashboardMaint, whereClauseDashBdBAQ, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseDashboardMaint=" + whereClauseDashboardMaint
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseDashBdBAQ=" + whereClauseDashBdBAQ
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DashboardMaintSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(productID, glbCompany, cgCCode, definitionID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   params += "productID=" + productID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "glbCompany=" + glbCompany
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "cgCCode=" + cgCCode
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "definitionID=" + definitionID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DashboardMaintSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DashboardMaintSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDashboardMaint(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDashboardMaint
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDashboardMaint
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDashboardMaint_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDashboardMaint_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DashboardMaintSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDashBdBAQ(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDashBdBAQ
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDashBdBAQ
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDashBdBAQ_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDashBdBAQ_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DashboardMaintSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DashboardMaintSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DashboardMaintSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DashboardMaintSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DashboardMaintSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DashboardMaintSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_DashBdBAQRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_DashBdBAQRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_DashboardMaintListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_DashboardMaintListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_DashboardMaintRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_DashboardMaintRow] = obj["value"]
      pass

class Ice_Tablesets_DashBdBAQRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProductID:str = obj["ProductID"]
      """  VN - Vantage, VS - Vista  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in identify from whch company this BAQ originated.  """  
      self.DefinitionID:str = obj["DefinitionID"]
      """  Dashboard Definition ID  """  
      self.QueryID:str = obj["QueryID"]
      """  Query ID  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group / Country Code for CSF  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_DashboardMaintListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProductID:str = obj["ProductID"]
      """  VN - Vantage, VS - Vista  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in identify from whch company this BAQ originated.  """  
      self.DefinitionID:str = obj["DefinitionID"]
      """  Dashboard Definition ID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.LastUpdated:str = obj["LastUpdated"]
      """  Last Updated Date  """  
      self.LastUpdatedBy:str = obj["LastUpdatedBy"]
      """  Last Update By  """  
      self.DashBdVersion:str = obj["DashBdVersion"]
      """  Dashboard Version  """  
      self.DataBaseVersion:int = obj["DataBaseVersion"]
      """  Database Version  """  
      self.Delivered:bool = obj["Delivered"]
      """  Indicates this dashboard is a system dashboard and any changes will be wiped with the next service pack.  """  
      self.MobileAccess:bool = obj["MobileAccess"]
      """  Indicates whether this Dashboard is available on the mobile menu.  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.LastDeployedDate:str = obj["LastDeployedDate"]
      """  LastDeployedDate  """  
      self.LastDeployedBy:str = obj["LastDeployedBy"]
      """  LastDeployedBy  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Deployed:bool = obj["Deployed"]
      """  Deployed  """  
      self.Error:str = obj["Error"]
      self.Generated:bool = obj["Generated"]
      """  Generated  """  
      self.Selected:bool = obj["Selected"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_DashboardMaintRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProductID:str = obj["ProductID"]
      """  VN - Vantage, VS - Vista  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in identify from whch company this BAQ originated.  """  
      self.DefinitionID:str = obj["DefinitionID"]
      """  Dashboard Definition ID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.LastUpdated:str = obj["LastUpdated"]
      """  Last Updated Date  """  
      self.LastUpdatedBy:str = obj["LastUpdatedBy"]
      """  Last Update By  """  
      self.DashBdVersion:str = obj["DashBdVersion"]
      """  Dashboard Version  """  
      self.DataBaseVersion:int = obj["DataBaseVersion"]
      """  Database Version  """  
      self.Delivered:bool = obj["Delivered"]
      """  Indicates this dashboard is a system dashboard and any changes will be wiped with the next service pack.  """  
      self.MobileAccess:bool = obj["MobileAccess"]
      """  Indicates whether this Dashboard is available on the mobile menu.  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.LastDeployedDate:str = obj["LastDeployedDate"]
      """  LastDeployedDate  """  
      self.LastDeployedBy:str = obj["LastDeployedBy"]
      """  LastDeployedBy  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Deployed:bool = obj["Deployed"]
      """  Deployed  """  
      self.Error:str = obj["Error"]
      self.Generated:bool = obj["Generated"]
      """  Generated  """  
      self.Selected:bool = obj["Selected"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   productID
   glbCompany
   cgCCode
   definitionID
   """  
   def __init__(self, obj):
      self.productID:str = obj["productID"]
      self.glbCompany:str = obj["glbCompany"]
      self.cgCCode:str = obj["cgCCode"]
      self.definitionID:str = obj["definitionID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class GetByID_input:
   """ Required : 
   productID
   glbCompany
   cgCCode
   definitionID
   """  
   def __init__(self, obj):
      self.productID:str = obj["productID"]
      self.glbCompany:str = obj["glbCompany"]
      self.cgCCode:str = obj["cgCCode"]
      self.definitionID:str = obj["definitionID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_DashboardMaintTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_DashboardMaintTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_DashboardMaintTableset] = obj["returnObj"]
      pass

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
      self.returnObj:list[Ice_Tablesets_DashboardMaintListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewDashBdBAQ_input:
   """ Required : 
   ds
   productID
   glbCompany
   cgCCode
   definitionID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_DashboardMaintTableset] = obj["ds"]
      self.productID:str = obj["productID"]
      self.glbCompany:str = obj["glbCompany"]
      self.cgCCode:str = obj["cgCCode"]
      self.definitionID:str = obj["definitionID"]
      pass

class GetNewDashBdBAQ_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_DashboardMaintTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewDashboardMaint_input:
   """ Required : 
   ds
   productID
   glbCompany
   cgCCode
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_DashboardMaintTableset] = obj["ds"]
      self.productID:str = obj["productID"]
      self.glbCompany:str = obj["glbCompany"]
      self.cgCCode:str = obj["cgCCode"]
      pass

class GetNewDashboardMaint_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_DashboardMaintTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseDashboardMaint
   whereClauseDashBdBAQ
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseDashboardMaint:str = obj["whereClauseDashboardMaint"]
      self.whereClauseDashBdBAQ:str = obj["whereClauseDashBdBAQ"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_DashboardMaintTableset] = obj["returnObj"]
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

class Ice_Tablesets_DashBdBAQRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProductID:str = obj["ProductID"]
      """  VN - Vantage, VS - Vista  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in identify from whch company this BAQ originated.  """  
      self.DefinitionID:str = obj["DefinitionID"]
      """  Dashboard Definition ID  """  
      self.QueryID:str = obj["QueryID"]
      """  Query ID  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group / Country Code for CSF  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_DashboardMaintListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProductID:str = obj["ProductID"]
      """  VN - Vantage, VS - Vista  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in identify from whch company this BAQ originated.  """  
      self.DefinitionID:str = obj["DefinitionID"]
      """  Dashboard Definition ID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.LastUpdated:str = obj["LastUpdated"]
      """  Last Updated Date  """  
      self.LastUpdatedBy:str = obj["LastUpdatedBy"]
      """  Last Update By  """  
      self.DashBdVersion:str = obj["DashBdVersion"]
      """  Dashboard Version  """  
      self.DataBaseVersion:int = obj["DataBaseVersion"]
      """  Database Version  """  
      self.Delivered:bool = obj["Delivered"]
      """  Indicates this dashboard is a system dashboard and any changes will be wiped with the next service pack.  """  
      self.MobileAccess:bool = obj["MobileAccess"]
      """  Indicates whether this Dashboard is available on the mobile menu.  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.LastDeployedDate:str = obj["LastDeployedDate"]
      """  LastDeployedDate  """  
      self.LastDeployedBy:str = obj["LastDeployedBy"]
      """  LastDeployedBy  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Deployed:bool = obj["Deployed"]
      """  Deployed  """  
      self.Error:str = obj["Error"]
      self.Generated:bool = obj["Generated"]
      """  Generated  """  
      self.Selected:bool = obj["Selected"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_DashboardMaintListTableset:
   def __init__(self, obj):
      self.DashboardMaintList:list[Ice_Tablesets_DashboardMaintListRow] = obj["DashboardMaintList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_DashboardMaintRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProductID:str = obj["ProductID"]
      """  VN - Vantage, VS - Vista  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in identify from whch company this BAQ originated.  """  
      self.DefinitionID:str = obj["DefinitionID"]
      """  Dashboard Definition ID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.LastUpdated:str = obj["LastUpdated"]
      """  Last Updated Date  """  
      self.LastUpdatedBy:str = obj["LastUpdatedBy"]
      """  Last Update By  """  
      self.DashBdVersion:str = obj["DashBdVersion"]
      """  Dashboard Version  """  
      self.DataBaseVersion:int = obj["DataBaseVersion"]
      """  Database Version  """  
      self.Delivered:bool = obj["Delivered"]
      """  Indicates this dashboard is a system dashboard and any changes will be wiped with the next service pack.  """  
      self.MobileAccess:bool = obj["MobileAccess"]
      """  Indicates whether this Dashboard is available on the mobile menu.  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.LastDeployedDate:str = obj["LastDeployedDate"]
      """  LastDeployedDate  """  
      self.LastDeployedBy:str = obj["LastDeployedBy"]
      """  LastDeployedBy  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Deployed:bool = obj["Deployed"]
      """  Deployed  """  
      self.Error:str = obj["Error"]
      self.Generated:bool = obj["Generated"]
      """  Generated  """  
      self.Selected:bool = obj["Selected"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_DashboardMaintTableset:
   def __init__(self, obj):
      self.DashboardMaint:list[Ice_Tablesets_DashboardMaintRow] = obj["DashboardMaint"]
      self.DashBdBAQ:list[Ice_Tablesets_DashBdBAQRow] = obj["DashBdBAQ"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_UpdExtDashboardMaintTableset:
   def __init__(self, obj):
      self.DashboardMaint:list[Ice_Tablesets_DashboardMaintRow] = obj["DashboardMaint"]
      self.DashBdBAQ:list[Ice_Tablesets_DashBdBAQRow] = obj["DashBdBAQ"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtDashboardMaintTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtDashboardMaintTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_DashboardMaintTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_DashboardMaintTableset] = obj["ds"]
      pass

      """  output parameters  """  

