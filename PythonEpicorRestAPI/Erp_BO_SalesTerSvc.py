import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.SalesTerSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTerSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTerSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_SalesTers(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SalesTers items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SalesTers
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SalesTerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTerSvc/SalesTers",headers=creds) as resp:
           return await resp.json()

async def post_SalesTers(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SalesTers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SalesTerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SalesTerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTerSvc/SalesTers", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SalesTers_Company_TerritoryID(Company, TerritoryID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SalesTer item
   Description: Calls GetByID to retrieve the SalesTer item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SalesTer
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TerritoryID: Desc: TerritoryID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SalesTerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTerSvc/SalesTers(" + Company + "," + TerritoryID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SalesTers_Company_TerritoryID(Company, TerritoryID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SalesTer for the service
   Description: Calls UpdateExt to update SalesTer. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SalesTer
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TerritoryID: Desc: TerritoryID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SalesTerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.SalesTerSvc/SalesTers(" + Company + "," + TerritoryID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SalesTers_Company_TerritoryID(Company, TerritoryID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SalesTer item
   Description: Call UpdateExt to delete SalesTer item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SalesTer
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TerritoryID: Desc: TerritoryID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.SalesTerSvc/SalesTers(" + Company + "," + TerritoryID + ")",headers=creds) as resp:
           return await resp.json()

async def get_SalesTers_Company_TerritoryID_SalesTBDs(Company, TerritoryID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get SalesTBDs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_SalesTBDs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TerritoryID: Desc: TerritoryID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SalesTBDRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTerSvc/SalesTers(" + Company + "," + TerritoryID + ")/SalesTBDs",headers=creds) as resp:
           return await resp.json()

async def get_SalesTers_Company_TerritoryID_SalesTBDs_Company_TerritoryID_CountryNum_State_StartZip_EndZip(Company, TerritoryID, CountryNum, State, StartZip, EndZip, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SalesTBD item
   Description: Calls GetByID to retrieve the SalesTBD item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SalesTBD1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TerritoryID: Desc: TerritoryID   Required: True   Allow empty value : True
      :param CountryNum: Desc: CountryNum   Required: True
      :param State: Desc: State   Required: True   Allow empty value : True
      :param StartZip: Desc: StartZip   Required: True   Allow empty value : True
      :param EndZip: Desc: EndZip   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SalesTBDRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTerSvc/SalesTers(" + Company + "," + TerritoryID + ")/SalesTBDs(" + Company + "," + TerritoryID + "," + CountryNum + "," + State + "," + StartZip + "," + EndZip + ")",headers=creds) as resp:
           return await resp.json()

async def get_SalesTers_Company_TerritoryID_SalesTRPs(Company, TerritoryID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get SalesTRPs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_SalesTRPs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TerritoryID: Desc: TerritoryID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SalesTRPRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTerSvc/SalesTers(" + Company + "," + TerritoryID + ")/SalesTRPs",headers=creds) as resp:
           return await resp.json()

async def get_SalesTers_Company_TerritoryID_SalesTRPs_Company_TerritoryID_SalesRepCode(Company, TerritoryID, SalesRepCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SalesTRP item
   Description: Calls GetByID to retrieve the SalesTRP item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SalesTRP1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TerritoryID: Desc: TerritoryID   Required: True   Allow empty value : True
      :param SalesRepCode: Desc: SalesRepCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SalesTRPRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTerSvc/SalesTers(" + Company + "," + TerritoryID + ")/SalesTRPs(" + Company + "," + TerritoryID + "," + SalesRepCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_SalesTBDs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SalesTBDs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SalesTBDs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SalesTBDRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTerSvc/SalesTBDs",headers=creds) as resp:
           return await resp.json()

async def post_SalesTBDs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SalesTBDs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SalesTBDRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SalesTBDRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTerSvc/SalesTBDs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SalesTBDs_Company_TerritoryID_CountryNum_State_StartZip_EndZip(Company, TerritoryID, CountryNum, State, StartZip, EndZip, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SalesTBD item
   Description: Calls GetByID to retrieve the SalesTBD item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SalesTBD
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TerritoryID: Desc: TerritoryID   Required: True   Allow empty value : True
      :param CountryNum: Desc: CountryNum   Required: True
      :param State: Desc: State   Required: True   Allow empty value : True
      :param StartZip: Desc: StartZip   Required: True   Allow empty value : True
      :param EndZip: Desc: EndZip   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SalesTBDRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTerSvc/SalesTBDs(" + Company + "," + TerritoryID + "," + CountryNum + "," + State + "," + StartZip + "," + EndZip + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SalesTBDs_Company_TerritoryID_CountryNum_State_StartZip_EndZip(Company, TerritoryID, CountryNum, State, StartZip, EndZip, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SalesTBD for the service
   Description: Calls UpdateExt to update SalesTBD. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SalesTBD
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TerritoryID: Desc: TerritoryID   Required: True   Allow empty value : True
      :param CountryNum: Desc: CountryNum   Required: True
      :param State: Desc: State   Required: True   Allow empty value : True
      :param StartZip: Desc: StartZip   Required: True   Allow empty value : True
      :param EndZip: Desc: EndZip   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SalesTBDRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.SalesTerSvc/SalesTBDs(" + Company + "," + TerritoryID + "," + CountryNum + "," + State + "," + StartZip + "," + EndZip + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SalesTBDs_Company_TerritoryID_CountryNum_State_StartZip_EndZip(Company, TerritoryID, CountryNum, State, StartZip, EndZip, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SalesTBD item
   Description: Call UpdateExt to delete SalesTBD item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SalesTBD
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TerritoryID: Desc: TerritoryID   Required: True   Allow empty value : True
      :param CountryNum: Desc: CountryNum   Required: True
      :param State: Desc: State   Required: True   Allow empty value : True
      :param StartZip: Desc: StartZip   Required: True   Allow empty value : True
      :param EndZip: Desc: EndZip   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.SalesTerSvc/SalesTBDs(" + Company + "," + TerritoryID + "," + CountryNum + "," + State + "," + StartZip + "," + EndZip + ")",headers=creds) as resp:
           return await resp.json()

async def get_SalesTRPs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SalesTRPs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SalesTRPs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SalesTRPRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTerSvc/SalesTRPs",headers=creds) as resp:
           return await resp.json()

async def post_SalesTRPs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SalesTRPs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SalesTRPRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SalesTRPRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTerSvc/SalesTRPs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SalesTRPs_Company_TerritoryID_SalesRepCode(Company, TerritoryID, SalesRepCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SalesTRP item
   Description: Calls GetByID to retrieve the SalesTRP item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SalesTRP
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TerritoryID: Desc: TerritoryID   Required: True   Allow empty value : True
      :param SalesRepCode: Desc: SalesRepCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SalesTRPRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTerSvc/SalesTRPs(" + Company + "," + TerritoryID + "," + SalesRepCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SalesTRPs_Company_TerritoryID_SalesRepCode(Company, TerritoryID, SalesRepCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SalesTRP for the service
   Description: Calls UpdateExt to update SalesTRP. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SalesTRP
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TerritoryID: Desc: TerritoryID   Required: True   Allow empty value : True
      :param SalesRepCode: Desc: SalesRepCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SalesTRPRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.SalesTerSvc/SalesTRPs(" + Company + "," + TerritoryID + "," + SalesRepCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SalesTRPs_Company_TerritoryID_SalesRepCode(Company, TerritoryID, SalesRepCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SalesTRP item
   Description: Call UpdateExt to delete SalesTRP item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SalesTRP
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TerritoryID: Desc: TerritoryID   Required: True   Allow empty value : True
      :param SalesRepCode: Desc: SalesRepCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.SalesTerSvc/SalesTRPs(" + Company + "," + TerritoryID + "," + SalesRepCode + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SalesTerListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTerSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseSalesTer, whereClauseSalesTBD, whereClauseSalesTRP, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
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
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseSalesTer=" + whereClauseSalesTer
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseSalesTBD=" + whereClauseSalesTBD
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseSalesTRP=" + whereClauseSalesTRP
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTerSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(territoryID, epicorHeaders = None):
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
   params += "territoryID=" + territoryID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTerSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTerSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_AdjustTerritory(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AdjustTerritory
   Description: This method sets PendingTerritoryies to new Territory boundaries
   OperationID: AdjustTerritory
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AdjustTerritory_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AdjustTerritory_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckSecurity(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckSecurity
   Description: We want to know if the user has the permissions to retrieve the territory
   OperationID: CheckSecurity
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckSecurity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckSecurity_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckTerrSalesperson(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckTerrSalesperson
   Description: This method checks that the territory has at least one Salesperson before
allowing the user to leave the territory record
   OperationID: CheckTerrSalesperson
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckTerrSalesperson_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckTerrSalesperson_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ClearPending(epicorHeaders = None):
   """  
   Summary: Invoke method ClearPending
   Description: This method clears the pending territory updates from all customer/shipto's
   OperationID: ClearPending
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClearPending_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTerSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetByIDCustom(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByIDCustom
   Description: This method returns a single Territory (which can be inactive)
   OperationID: GetByIDCustom
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByIDCustom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByIDCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListCustom(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListCustom
   Description: This method returns a list of Territories, including inactive ones.
   OperationID: GetListCustom
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListCustom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSalesrepList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSalesrepList
   Description: This method called from Kinetic UI to gt list of SalesPer to exclude from combo selection
   OperationID: GetSalesrepList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSalesrepList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSalesrepList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListPlusRO(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListPlusRO
   Description: This method returns a list of Territories, including the Read-Only ones.
   OperationID: GetListPlusRO
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListPlusRO_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListPlusRO_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsCustom(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsCustom
   Description: This method returns a list of Territories, including inactive ones
   OperationID: GetRowsCustom
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsCustom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSalesRepInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSalesRepInfo
   Description: This method defaults the role code field in SalesTRP once salesRepCode is selected
   OperationID: GetSalesRepInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSalesRepInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSalesRepInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PostTerritories(epicorHeaders = None):
   """  
   Summary: Invoke method PostTerritories
   Description: This method posts the PendingTerritoryID to the actual TerritoryID for all Customer/ShipTo's.
   OperationID: PostTerritories
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/PostTerritories_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTerSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_ReassignTerritory(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ReassignTerritory
   Description: This method reassigns SalesPeople and Tasks to their new Territory or SalesPerson
   OperationID: ReassignTerritory
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ReassignTerritory_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReassignTerritory_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSalesTer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSalesTer
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSalesTer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSalesTer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSalesTer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSalesTBD(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSalesTBD
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSalesTBD
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSalesTBD_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSalesTBD_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSalesTRP(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSalesTRP
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSalesTRP
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSalesTRP_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSalesTRP_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTerSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTerSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTerSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTerSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTerSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SalesTBDRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SalesTBDRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SalesTRPRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SalesTRPRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SalesTerListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SalesTerListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SalesTerRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SalesTerRow] = obj["value"]
      pass

class Erp_Tablesets_SalesTBDRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TerritoryID:str = obj["TerritoryID"]
      """  Contains the SalesTer.TerritoryID value of the territory whose boundary you are defining.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Country.CountryNum value of the country used in defining the  territory's boundary.  """  
      self.CountryName:str = obj["CountryName"]
      """  Country name from the country table used in defining the territory's boundary.  """  
      self.State:str = obj["State"]
      """  State/Province component used in defining a territory's boundary.  """  
      self.StartZip:str = obj["StartZip"]
      """  Starting Zip Code/Postal Code value used when defining the territory's boundary.  """  
      self.EndZip:str = obj["EndZip"]
      """  Ending Zip Code/Postal Code value used when defining the territory's boundary.  """  
      self.GlobalSalesTBD:bool = obj["GlobalSalesTBD"]
      """  Marks this SalesTBD as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CountryNumDescription:str = obj["CountryNumDescription"]
      self.TerritoryIDTerritoryDesc:str = obj["TerritoryIDTerritoryDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SalesTRPRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TerritoryID:str = obj["TerritoryID"]
      """  This identifies what territory the Sales Rep is part of.  """  
      self.SalesRepCode:str = obj["SalesRepCode"]
      """  This SalesRep.SalesRepCode value of the salesperson assigned to this territory.  """  
      self.Name:str = obj["Name"]
      """  The salesperson's name.  """  
      self.RoleCode:str = obj["RoleCode"]
      """  The RoleCD.RoleCode value of the role that the salesperson will be performing in the territory.  """  
      self.GlobalSalesTRP:bool = obj["GlobalSalesTRP"]
      """  Marks this SalesTRP as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.NewSalesRepCode:str = obj["NewSalesRepCode"]
      """  New Salesperson  """  
      self.ActionType:str = obj["ActionType"]
      """  "Replace" or "Add"  """  
      self.ReassignTasks:bool = obj["ReassignTasks"]
      """  Reassign Open Tasks  """  
      self.Primary:bool = obj["Primary"]
      self.BitFlag:int = obj["BitFlag"]
      self.RoleCodeRoleDescription:str = obj["RoleCodeRoleDescription"]
      self.TerritoryIDTerritoryDesc:str = obj["TerritoryIDTerritoryDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SalesTerListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TerritoryID:str = obj["TerritoryID"]
      """  Unique identifier of the territory.  """  
      self.TerritoryDesc:str = obj["TerritoryDesc"]
      """  Description of the territory.  """  
      self.RegionCode:str = obj["RegionCode"]
      """  Region.RegionCode value of the Sales Region the territory is associated with.  """  
      self.Comment:str = obj["Comment"]
      """  Territory comments are intended to be internal comments about the specific territory and do not flow into any quotes, orders or reports.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates whether or not this territory can be assigned to new customers or quotes.  """  
      self.PrimeSalesRepCode:str = obj["PrimeSalesRepCode"]
      """  Contains the SalesTRP.SalesRepCode value of the primary salesperson for the territory.  """  
      self.DefTaskSetID:str = obj["DefTaskSetID"]
      """  Contains the TaskSet.TaskSetID value that will be used as the default task set by leads, opportunities and quotes associated with the territory.  """  
      self.ConsToPrim:bool = obj["ConsToPrim"]
      """  Consolidates pipeline information in the Salesperson Workbench to the territory's primary salesperson.  """  
      self.PrimeBillingTypeCD:str = obj["PrimeBillingTypeCD"]
      """  Contains the value of the primary billing type code for the prospect.  """  
      self.GlobalSalesTer:bool = obj["GlobalSalesTer"]
      """  Marks this SalesTer as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DefTaskTaskSetDescription:str = obj["DefTaskTaskSetDescription"]
      """  Description of the task set.  """  
      self.DefTaskWorkflowType:str = obj["DefTaskWorkflowType"]
      """  The type of workflow of this task set.  Possible values are "CRM" - CRM related tasks and "ECO" - ECO tasks  """  
      self.RegionDescription:str = obj["RegionDescription"]
      """  Description of the sales region.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SalesTerRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TerritoryID:str = obj["TerritoryID"]
      """  Unique identifier of the territory.  """  
      self.TerritoryDesc:str = obj["TerritoryDesc"]
      """  Description of the territory.  """  
      self.RegionCode:str = obj["RegionCode"]
      """  Region.RegionCode value of the Sales Region the territory is associated with.  """  
      self.Comment:str = obj["Comment"]
      """  Territory comments are intended to be internal comments about the specific territory and do not flow into any quotes, orders or reports.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates whether or not this territory can be assigned to new customers or quotes.  """  
      self.PrimeSalesRepCode:str = obj["PrimeSalesRepCode"]
      """  Contains the SalesTRP.SalesRepCode value of the primary salesperson for the territory.  """  
      self.DefTaskSetID:str = obj["DefTaskSetID"]
      """  Contains the TaskSet.TaskSetID value that will be used as the default task set by leads, opportunities and quotes associated with the territory.  """  
      self.ConsToPrim:bool = obj["ConsToPrim"]
      """  Consolidates pipeline information in the Salesperson Workbench to the territory's primary salesperson.  """  
      self.PrimeBillingTypeCD:str = obj["PrimeBillingTypeCD"]
      """  Contains the value of the primary billing type code for the prospect.  """  
      self.GlobalSalesTer:bool = obj["GlobalSalesTer"]
      """  Marks this SalesTer as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.DefTaskTaskSetDescription:str = obj["DefTaskTaskSetDescription"]
      self.DefTaskWorkflowType:str = obj["DefTaskWorkflowType"]
      self.RegionDescription:str = obj["RegionDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class AdjustTerritory_input:
   """ Required : 
   cTerritoryID
   """  
   def __init__(self, obj):
      self.cTerritoryID:str = obj["cTerritoryID"]
      """  Blank for All, otherwise specify the territory to adjust  """  
      pass

class AdjustTerritory_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.vMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckSecurity_input:
   """ Required : 
   cTerritoryID
   """  
   def __init__(self, obj):
      self.cTerritoryID:str = obj["cTerritoryID"]
      """  Territory to validate  """  
      pass

class CheckSecurity_output:
   def __init__(self, obj):
      pass

class CheckTerrSalesperson_input:
   """ Required : 
   cTerritoryID
   """  
   def __init__(self, obj):
      self.cTerritoryID:str = obj["cTerritoryID"]
      """  Territory to validate  """  
      pass

class CheckTerrSalesperson_output:
   def __init__(self, obj):
      pass

class ClearPending_output:
   def __init__(self, obj):
      pass

class DeleteByID_input:
   """ Required : 
   territoryID
   """  
   def __init__(self, obj):
      self.territoryID:str = obj["territoryID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_SalesTBDRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TerritoryID:str = obj["TerritoryID"]
      """  Contains the SalesTer.TerritoryID value of the territory whose boundary you are defining.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Country.CountryNum value of the country used in defining the  territory's boundary.  """  
      self.CountryName:str = obj["CountryName"]
      """  Country name from the country table used in defining the territory's boundary.  """  
      self.State:str = obj["State"]
      """  State/Province component used in defining a territory's boundary.  """  
      self.StartZip:str = obj["StartZip"]
      """  Starting Zip Code/Postal Code value used when defining the territory's boundary.  """  
      self.EndZip:str = obj["EndZip"]
      """  Ending Zip Code/Postal Code value used when defining the territory's boundary.  """  
      self.GlobalSalesTBD:bool = obj["GlobalSalesTBD"]
      """  Marks this SalesTBD as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CountryNumDescription:str = obj["CountryNumDescription"]
      self.TerritoryIDTerritoryDesc:str = obj["TerritoryIDTerritoryDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SalesTRPRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TerritoryID:str = obj["TerritoryID"]
      """  This identifies what territory the Sales Rep is part of.  """  
      self.SalesRepCode:str = obj["SalesRepCode"]
      """  This SalesRep.SalesRepCode value of the salesperson assigned to this territory.  """  
      self.Name:str = obj["Name"]
      """  The salesperson's name.  """  
      self.RoleCode:str = obj["RoleCode"]
      """  The RoleCD.RoleCode value of the role that the salesperson will be performing in the territory.  """  
      self.GlobalSalesTRP:bool = obj["GlobalSalesTRP"]
      """  Marks this SalesTRP as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.NewSalesRepCode:str = obj["NewSalesRepCode"]
      """  New Salesperson  """  
      self.ActionType:str = obj["ActionType"]
      """  "Replace" or "Add"  """  
      self.ReassignTasks:bool = obj["ReassignTasks"]
      """  Reassign Open Tasks  """  
      self.Primary:bool = obj["Primary"]
      self.BitFlag:int = obj["BitFlag"]
      self.RoleCodeRoleDescription:str = obj["RoleCodeRoleDescription"]
      self.TerritoryIDTerritoryDesc:str = obj["TerritoryIDTerritoryDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SalesTerListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TerritoryID:str = obj["TerritoryID"]
      """  Unique identifier of the territory.  """  
      self.TerritoryDesc:str = obj["TerritoryDesc"]
      """  Description of the territory.  """  
      self.RegionCode:str = obj["RegionCode"]
      """  Region.RegionCode value of the Sales Region the territory is associated with.  """  
      self.Comment:str = obj["Comment"]
      """  Territory comments are intended to be internal comments about the specific territory and do not flow into any quotes, orders or reports.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates whether or not this territory can be assigned to new customers or quotes.  """  
      self.PrimeSalesRepCode:str = obj["PrimeSalesRepCode"]
      """  Contains the SalesTRP.SalesRepCode value of the primary salesperson for the territory.  """  
      self.DefTaskSetID:str = obj["DefTaskSetID"]
      """  Contains the TaskSet.TaskSetID value that will be used as the default task set by leads, opportunities and quotes associated with the territory.  """  
      self.ConsToPrim:bool = obj["ConsToPrim"]
      """  Consolidates pipeline information in the Salesperson Workbench to the territory's primary salesperson.  """  
      self.PrimeBillingTypeCD:str = obj["PrimeBillingTypeCD"]
      """  Contains the value of the primary billing type code for the prospect.  """  
      self.GlobalSalesTer:bool = obj["GlobalSalesTer"]
      """  Marks this SalesTer as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DefTaskTaskSetDescription:str = obj["DefTaskTaskSetDescription"]
      """  Description of the task set.  """  
      self.DefTaskWorkflowType:str = obj["DefTaskWorkflowType"]
      """  The type of workflow of this task set.  Possible values are "CRM" - CRM related tasks and "ECO" - ECO tasks  """  
      self.RegionDescription:str = obj["RegionDescription"]
      """  Description of the sales region.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SalesTerListTableset:
   def __init__(self, obj):
      self.SalesTerList:list[Erp_Tablesets_SalesTerListRow] = obj["SalesTerList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_SalesTerRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TerritoryID:str = obj["TerritoryID"]
      """  Unique identifier of the territory.  """  
      self.TerritoryDesc:str = obj["TerritoryDesc"]
      """  Description of the territory.  """  
      self.RegionCode:str = obj["RegionCode"]
      """  Region.RegionCode value of the Sales Region the territory is associated with.  """  
      self.Comment:str = obj["Comment"]
      """  Territory comments are intended to be internal comments about the specific territory and do not flow into any quotes, orders or reports.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates whether or not this territory can be assigned to new customers or quotes.  """  
      self.PrimeSalesRepCode:str = obj["PrimeSalesRepCode"]
      """  Contains the SalesTRP.SalesRepCode value of the primary salesperson for the territory.  """  
      self.DefTaskSetID:str = obj["DefTaskSetID"]
      """  Contains the TaskSet.TaskSetID value that will be used as the default task set by leads, opportunities and quotes associated with the territory.  """  
      self.ConsToPrim:bool = obj["ConsToPrim"]
      """  Consolidates pipeline information in the Salesperson Workbench to the territory's primary salesperson.  """  
      self.PrimeBillingTypeCD:str = obj["PrimeBillingTypeCD"]
      """  Contains the value of the primary billing type code for the prospect.  """  
      self.GlobalSalesTer:bool = obj["GlobalSalesTer"]
      """  Marks this SalesTer as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.DefTaskTaskSetDescription:str = obj["DefTaskTaskSetDescription"]
      self.DefTaskWorkflowType:str = obj["DefTaskWorkflowType"]
      self.RegionDescription:str = obj["RegionDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SalesTerTableset:
   def __init__(self, obj):
      self.SalesTer:list[Erp_Tablesets_SalesTerRow] = obj["SalesTer"]
      self.SalesTBD:list[Erp_Tablesets_SalesTBDRow] = obj["SalesTBD"]
      self.SalesTRP:list[Erp_Tablesets_SalesTRPRow] = obj["SalesTRP"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtSalesTerTableset:
   def __init__(self, obj):
      self.SalesTer:list[Erp_Tablesets_SalesTerRow] = obj["SalesTer"]
      self.SalesTBD:list[Erp_Tablesets_SalesTBDRow] = obj["SalesTBD"]
      self.SalesTRP:list[Erp_Tablesets_SalesTRPRow] = obj["SalesTRP"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByIDCustom_input:
   """ Required : 
   territoryID
   """  
   def __init__(self, obj):
      self.territoryID:str = obj["territoryID"]
      """  The territory code  """  
      pass

class GetByIDCustom_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SalesTerTableset] = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   territoryID
   """  
   def __init__(self, obj):
      self.territoryID:str = obj["territoryID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SalesTerTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_SalesTerTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_SalesTerTableset] = obj["returnObj"]
      pass

class GetListCustom_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  The criteria  """  
      self.pageSize:int = obj["pageSize"]
      """  Size of a page  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolute page  """  
      pass

class GetListCustom_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SalesTerListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetListPlusRO_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  The criteria  """  
      self.pageSize:int = obj["pageSize"]
      """  Size of a page  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolute page  """  
      pass

class GetListPlusRO_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SalesTerListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
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
      self.returnObj:list[Erp_Tablesets_SalesTerListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewSalesTBD_input:
   """ Required : 
   ds
   territoryID
   countryNum
   state
   startZip
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SalesTerTableset] = obj["ds"]
      self.territoryID:str = obj["territoryID"]
      self.countryNum:int = obj["countryNum"]
      self.state:str = obj["state"]
      self.startZip:str = obj["startZip"]
      pass

class GetNewSalesTBD_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SalesTerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewSalesTRP_input:
   """ Required : 
   ds
   territoryID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SalesTerTableset] = obj["ds"]
      self.territoryID:str = obj["territoryID"]
      pass

class GetNewSalesTRP_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SalesTerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewSalesTer_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SalesTerTableset] = obj["ds"]
      pass

class GetNewSalesTer_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SalesTerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRowsCustom_input:
   """ Required : 
   whereClauseSalesTer
   whereClauseSalesTBD
   whereClauseSalesTRP
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseSalesTer:str = obj["whereClauseSalesTer"]
      """  The criteria  """  
      self.whereClauseSalesTBD:str = obj["whereClauseSalesTBD"]
      """  The TBD criteria  """  
      self.whereClauseSalesTRP:str = obj["whereClauseSalesTRP"]
      """  The TRP criteria  """  
      self.pageSize:int = obj["pageSize"]
      """  Size of a page  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolute page  """  
      pass

class GetRowsCustom_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SalesTerTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseSalesTer
   whereClauseSalesTBD
   whereClauseSalesTRP
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseSalesTer:str = obj["whereClauseSalesTer"]
      self.whereClauseSalesTBD:str = obj["whereClauseSalesTBD"]
      self.whereClauseSalesTRP:str = obj["whereClauseSalesTRP"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SalesTerTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSalesRepInfo_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SalesTerTableset] = obj["ds"]
      pass

class GetSalesRepInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SalesTerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetSalesrepList_input:
   """ Required : 
   terrID
   """  
   def __init__(self, obj):
      self.terrID:str = obj["terrID"]
      """  Sales territory ID.  """  
      pass

class GetSalesrepList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.salesRepList:str = obj["parameters"]
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

class PostTerritories_output:
   def __init__(self, obj):
      pass

class ReassignTerritory_input:
   """ Required : 
   cTerritoryId
   cSalesRepCode
   cNewSalesRepCode
   cActionType
   lReassignTasks
   """  
   def __init__(self, obj):
      self.cTerritoryId:str = obj["cTerritoryId"]
      """  Territory Id to update  """  
      self.cSalesRepCode:str = obj["cSalesRepCode"]
      """  Current SalesPerson  """  
      self.cNewSalesRepCode:str = obj["cNewSalesRepCode"]
      """  New SalesPerson  """  
      self.cActionType:str = obj["cActionType"]
      self.lReassignTasks:bool = obj["lReassignTasks"]
      """  If yes, then Tasks will be reassigned to the new SalesPerson  """  
      pass

class ReassignTerritory_output:
   def __init__(self, obj):
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtSalesTerTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtSalesTerTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SalesTerTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SalesTerTableset] = obj["ds"]
      pass

      """  output parameters  """  

