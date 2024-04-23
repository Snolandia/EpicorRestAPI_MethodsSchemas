import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.WhseGroupSvc
# Description: WhseGroup Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_WhseGroups(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get WhseGroups items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_WhseGroups
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WhseGroupRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/WhseGroups",headers=creds) as resp:
           return await resp.json()

async def post_WhseGroups(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_WhseGroups
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.WhseGroupRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.WhseGroupRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/WhseGroups", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_WhseGroups_Company_WhseGroupCode(Company, WhseGroupCode, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the WhseGroup item
   Description: Calls GetByID to retrieve the WhseGroup item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WhseGroup
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WhseGroupCode: Desc: WhseGroupCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.WhseGroupRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/WhseGroups(" + Company + "," + WhseGroupCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_WhseGroups_Company_WhseGroupCode(Company, WhseGroupCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update WhseGroup for the service
   Description: Calls UpdateExt to update WhseGroup. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_WhseGroup
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WhseGroupCode: Desc: WhseGroupCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.WhseGroupRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/WhseGroups(" + Company + "," + WhseGroupCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_WhseGroups_Company_WhseGroupCode(Company, WhseGroupCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete WhseGroup item
   Description: Call UpdateExt to delete WhseGroup item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_WhseGroup
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WhseGroupCode: Desc: WhseGroupCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/WhseGroups(" + Company + "," + WhseGroupCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_WhseGroups_Company_WhseGroupCode_WhseGroupAttrs(Company, WhseGroupCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get WhseGroupAttrs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_WhseGroupAttrs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WhseGroupCode: Desc: WhseGroupCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WhseGroupAttrRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/WhseGroups(" + Company + "," + WhseGroupCode + ")/WhseGroupAttrs",headers=creds) as resp:
           return await resp.json()

async def get_WhseGroups_Company_WhseGroupCode_WhseGroupAttrs_Company_WhseGroupCode_AttrCode(Company, WhseGroupCode, AttrCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the WhseGroupAttr item
   Description: Calls GetByID to retrieve the WhseGroupAttr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WhseGroupAttr1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WhseGroupCode: Desc: WhseGroupCode   Required: True   Allow empty value : True
      :param AttrCode: Desc: AttrCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.WhseGroupAttrRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/WhseGroups(" + Company + "," + WhseGroupCode + ")/WhseGroupAttrs(" + Company + "," + WhseGroupCode + "," + AttrCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_WhseGroups_Company_WhseGroupCode_WhseGroupEmps(Company, WhseGroupCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get WhseGroupEmps items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_WhseGroupEmps1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WhseGroupCode: Desc: WhseGroupCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WhseGroupEmpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/WhseGroups(" + Company + "," + WhseGroupCode + ")/WhseGroupEmps",headers=creds) as resp:
           return await resp.json()

async def get_WhseGroups_Company_WhseGroupCode_WhseGroupEmps_Company_WhseGroupCode_EmpID(Company, WhseGroupCode, EmpID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the WhseGroupEmp item
   Description: Calls GetByID to retrieve the WhseGroupEmp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WhseGroupEmp1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WhseGroupCode: Desc: WhseGroupCode   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.WhseGroupEmpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/WhseGroups(" + Company + "," + WhseGroupCode + ")/WhseGroupEmps(" + Company + "," + WhseGroupCode + "," + EmpID + ")",headers=creds) as resp:
           return await resp.json()

async def get_WhseGroups_Company_WhseGroupCode_WhseGroupTrans(Company, WhseGroupCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get WhseGroupTrans items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_WhseGroupTrans1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WhseGroupCode: Desc: WhseGroupCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WhseGroupTransRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/WhseGroups(" + Company + "," + WhseGroupCode + ")/WhseGroupTrans",headers=creds) as resp:
           return await resp.json()

async def get_WhseGroups_Company_WhseGroupCode_WhseGroupTrans_Company_WhseGroupCode_TransCode(Company, WhseGroupCode, TransCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the WhseGroupTran item
   Description: Calls GetByID to retrieve the WhseGroupTran item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WhseGroupTran1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WhseGroupCode: Desc: WhseGroupCode   Required: True   Allow empty value : True
      :param TransCode: Desc: TransCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.WhseGroupTransRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/WhseGroups(" + Company + "," + WhseGroupCode + ")/WhseGroupTrans(" + Company + "," + WhseGroupCode + "," + TransCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_WhseGroups_Company_WhseGroupCode_WhseGroupWhses(Company, WhseGroupCode, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get WhseGroupWhses items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_WhseGroupWhses1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WhseGroupCode: Desc: WhseGroupCode   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WhseGroupWhseRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/WhseGroups(" + Company + "," + WhseGroupCode + ")/WhseGroupWhses",headers=creds) as resp:
           return await resp.json()

async def get_WhseGroups_Company_WhseGroupCode_WhseGroupWhses_Company_WhseGroupCode_WarehouseCode(Company, WhseGroupCode, WarehouseCode, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the WhseGroupWhse item
   Description: Calls GetByID to retrieve the WhseGroupWhse item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WhseGroupWhse1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WhseGroupCode: Desc: WhseGroupCode   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.WhseGroupWhseRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/WhseGroups(" + Company + "," + WhseGroupCode + ")/WhseGroupWhses(" + Company + "," + WhseGroupCode + "," + WarehouseCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_WhseGroupAttrs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get WhseGroupAttrs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_WhseGroupAttrs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WhseGroupAttrRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/WhseGroupAttrs",headers=creds) as resp:
           return await resp.json()

async def post_WhseGroupAttrs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_WhseGroupAttrs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.WhseGroupAttrRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.WhseGroupAttrRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/WhseGroupAttrs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_WhseGroupAttrs_Company_WhseGroupCode_AttrCode(Company, WhseGroupCode, AttrCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the WhseGroupAttr item
   Description: Calls GetByID to retrieve the WhseGroupAttr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WhseGroupAttr
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WhseGroupCode: Desc: WhseGroupCode   Required: True   Allow empty value : True
      :param AttrCode: Desc: AttrCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.WhseGroupAttrRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/WhseGroupAttrs(" + Company + "," + WhseGroupCode + "," + AttrCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_WhseGroupAttrs_Company_WhseGroupCode_AttrCode(Company, WhseGroupCode, AttrCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update WhseGroupAttr for the service
   Description: Calls UpdateExt to update WhseGroupAttr. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_WhseGroupAttr
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WhseGroupCode: Desc: WhseGroupCode   Required: True   Allow empty value : True
      :param AttrCode: Desc: AttrCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.WhseGroupAttrRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/WhseGroupAttrs(" + Company + "," + WhseGroupCode + "," + AttrCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_WhseGroupAttrs_Company_WhseGroupCode_AttrCode(Company, WhseGroupCode, AttrCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete WhseGroupAttr item
   Description: Call UpdateExt to delete WhseGroupAttr item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_WhseGroupAttr
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WhseGroupCode: Desc: WhseGroupCode   Required: True   Allow empty value : True
      :param AttrCode: Desc: AttrCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/WhseGroupAttrs(" + Company + "," + WhseGroupCode + "," + AttrCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_WhseGroupEmps(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get WhseGroupEmps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_WhseGroupEmps
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WhseGroupEmpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/WhseGroupEmps",headers=creds) as resp:
           return await resp.json()

async def post_WhseGroupEmps(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_WhseGroupEmps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.WhseGroupEmpRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.WhseGroupEmpRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/WhseGroupEmps", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_WhseGroupEmps_Company_WhseGroupCode_EmpID(Company, WhseGroupCode, EmpID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the WhseGroupEmp item
   Description: Calls GetByID to retrieve the WhseGroupEmp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WhseGroupEmp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WhseGroupCode: Desc: WhseGroupCode   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.WhseGroupEmpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/WhseGroupEmps(" + Company + "," + WhseGroupCode + "," + EmpID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_WhseGroupEmps_Company_WhseGroupCode_EmpID(Company, WhseGroupCode, EmpID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update WhseGroupEmp for the service
   Description: Calls UpdateExt to update WhseGroupEmp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_WhseGroupEmp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WhseGroupCode: Desc: WhseGroupCode   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.WhseGroupEmpRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/WhseGroupEmps(" + Company + "," + WhseGroupCode + "," + EmpID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_WhseGroupEmps_Company_WhseGroupCode_EmpID(Company, WhseGroupCode, EmpID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete WhseGroupEmp item
   Description: Call UpdateExt to delete WhseGroupEmp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_WhseGroupEmp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WhseGroupCode: Desc: WhseGroupCode   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/WhseGroupEmps(" + Company + "," + WhseGroupCode + "," + EmpID + ")",headers=creds) as resp:
           return await resp.json()

async def get_WhseGroupTrans(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get WhseGroupTrans items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_WhseGroupTrans
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WhseGroupTransRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/WhseGroupTrans",headers=creds) as resp:
           return await resp.json()

async def post_WhseGroupTrans(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_WhseGroupTrans
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.WhseGroupTransRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.WhseGroupTransRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/WhseGroupTrans", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_WhseGroupTrans_Company_WhseGroupCode_TransCode(Company, WhseGroupCode, TransCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the WhseGroupTran item
   Description: Calls GetByID to retrieve the WhseGroupTran item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WhseGroupTran
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WhseGroupCode: Desc: WhseGroupCode   Required: True   Allow empty value : True
      :param TransCode: Desc: TransCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.WhseGroupTransRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/WhseGroupTrans(" + Company + "," + WhseGroupCode + "," + TransCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_WhseGroupTrans_Company_WhseGroupCode_TransCode(Company, WhseGroupCode, TransCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update WhseGroupTran for the service
   Description: Calls UpdateExt to update WhseGroupTran. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_WhseGroupTran
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WhseGroupCode: Desc: WhseGroupCode   Required: True   Allow empty value : True
      :param TransCode: Desc: TransCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.WhseGroupTransRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/WhseGroupTrans(" + Company + "," + WhseGroupCode + "," + TransCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_WhseGroupTrans_Company_WhseGroupCode_TransCode(Company, WhseGroupCode, TransCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete WhseGroupTran item
   Description: Call UpdateExt to delete WhseGroupTran item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_WhseGroupTran
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WhseGroupCode: Desc: WhseGroupCode   Required: True   Allow empty value : True
      :param TransCode: Desc: TransCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/WhseGroupTrans(" + Company + "," + WhseGroupCode + "," + TransCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_WhseGroupWhses(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get WhseGroupWhses items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_WhseGroupWhses
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WhseGroupWhseRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/WhseGroupWhses",headers=creds) as resp:
           return await resp.json()

async def post_WhseGroupWhses(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_WhseGroupWhses
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.WhseGroupWhseRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.WhseGroupWhseRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/WhseGroupWhses", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_WhseGroupWhses_Company_WhseGroupCode_WarehouseCode(Company, WhseGroupCode, WarehouseCode, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the WhseGroupWhse item
   Description: Calls GetByID to retrieve the WhseGroupWhse item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WhseGroupWhse
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WhseGroupCode: Desc: WhseGroupCode   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.WhseGroupWhseRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/WhseGroupWhses(" + Company + "," + WhseGroupCode + "," + WarehouseCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_WhseGroupWhses_Company_WhseGroupCode_WarehouseCode(Company, WhseGroupCode, WarehouseCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update WhseGroupWhse for the service
   Description: Calls UpdateExt to update WhseGroupWhse. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_WhseGroupWhse
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WhseGroupCode: Desc: WhseGroupCode   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.WhseGroupWhseRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/WhseGroupWhses(" + Company + "," + WhseGroupCode + "," + WarehouseCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_WhseGroupWhses_Company_WhseGroupCode_WarehouseCode(Company, WhseGroupCode, WarehouseCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete WhseGroupWhse item
   Description: Call UpdateExt to delete WhseGroupWhse item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_WhseGroupWhse
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WhseGroupCode: Desc: WhseGroupCode   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/WhseGroupWhses(" + Company + "," + WhseGroupCode + "," + WarehouseCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_WhseGroupWhses_Company_WhseGroupCode_WarehouseCode_WhseGroupBins(Company, WhseGroupCode, WarehouseCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get WhseGroupBins items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_WhseGroupBins1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WhseGroupCode: Desc: WhseGroupCode   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WhseGroupBinRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/WhseGroupWhses(" + Company + "," + WhseGroupCode + "," + WarehouseCode + ")/WhseGroupBins",headers=creds) as resp:
           return await resp.json()

async def get_WhseGroupWhses_Company_WhseGroupCode_WarehouseCode_WhseGroupBins_Company_WhseGroupCode_WarehouseCode_BinNum(Company, WhseGroupCode, WarehouseCode, BinNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the WhseGroupBin item
   Description: Calls GetByID to retrieve the WhseGroupBin item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WhseGroupBin1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WhseGroupCode: Desc: WhseGroupCode   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param BinNum: Desc: BinNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.WhseGroupBinRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/WhseGroupWhses(" + Company + "," + WhseGroupCode + "," + WarehouseCode + ")/WhseGroupBins(" + Company + "," + WhseGroupCode + "," + WarehouseCode + "," + BinNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_WhseGroupWhses_Company_WhseGroupCode_WarehouseCode_WhseGroupBinZones(Company, WhseGroupCode, WarehouseCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get WhseGroupBinZones items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_WhseGroupBinZones1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WhseGroupCode: Desc: WhseGroupCode   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WhseGroupBinZoneRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/WhseGroupWhses(" + Company + "," + WhseGroupCode + "," + WarehouseCode + ")/WhseGroupBinZones",headers=creds) as resp:
           return await resp.json()

async def get_WhseGroupWhses_Company_WhseGroupCode_WarehouseCode_WhseGroupBinZones_Company_WhseGroupCode_WarehouseCode_ZoneID(Company, WhseGroupCode, WarehouseCode, ZoneID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the WhseGroupBinZone item
   Description: Calls GetByID to retrieve the WhseGroupBinZone item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WhseGroupBinZone1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WhseGroupCode: Desc: WhseGroupCode   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param ZoneID: Desc: ZoneID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.WhseGroupBinZoneRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/WhseGroupWhses(" + Company + "," + WhseGroupCode + "," + WarehouseCode + ")/WhseGroupBinZones(" + Company + "," + WhseGroupCode + "," + WarehouseCode + "," + ZoneID + ")",headers=creds) as resp:
           return await resp.json()

async def get_WhseGroupWhses_Company_WhseGroupCode_WarehouseCode_WhseGroupItems(Company, WhseGroupCode, WarehouseCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get WhseGroupItems items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_WhseGroupItems1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WhseGroupCode: Desc: WhseGroupCode   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WhseGroupItemRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/WhseGroupWhses(" + Company + "," + WhseGroupCode + "," + WarehouseCode + ")/WhseGroupItems",headers=creds) as resp:
           return await resp.json()

async def get_WhseGroupWhses_Company_WhseGroupCode_WarehouseCode_WhseGroupItems_Company_WhseGroupCode_WarehouseCode_ItemClass_ItemCode(Company, WhseGroupCode, WarehouseCode, ItemClass, ItemCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the WhseGroupItem item
   Description: Calls GetByID to retrieve the WhseGroupItem item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WhseGroupItem1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WhseGroupCode: Desc: WhseGroupCode   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param ItemClass: Desc: ItemClass   Required: True   Allow empty value : True
      :param ItemCode: Desc: ItemCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.WhseGroupItemRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/WhseGroupWhses(" + Company + "," + WhseGroupCode + "," + WarehouseCode + ")/WhseGroupItems(" + Company + "," + WhseGroupCode + "," + WarehouseCode + "," + ItemClass + "," + ItemCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_WhseGroupBins(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get WhseGroupBins items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_WhseGroupBins
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WhseGroupBinRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/WhseGroupBins",headers=creds) as resp:
           return await resp.json()

async def post_WhseGroupBins(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_WhseGroupBins
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.WhseGroupBinRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.WhseGroupBinRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/WhseGroupBins", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_WhseGroupBins_Company_WhseGroupCode_WarehouseCode_BinNum(Company, WhseGroupCode, WarehouseCode, BinNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the WhseGroupBin item
   Description: Calls GetByID to retrieve the WhseGroupBin item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WhseGroupBin
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WhseGroupCode: Desc: WhseGroupCode   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param BinNum: Desc: BinNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.WhseGroupBinRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/WhseGroupBins(" + Company + "," + WhseGroupCode + "," + WarehouseCode + "," + BinNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_WhseGroupBins_Company_WhseGroupCode_WarehouseCode_BinNum(Company, WhseGroupCode, WarehouseCode, BinNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update WhseGroupBin for the service
   Description: Calls UpdateExt to update WhseGroupBin. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_WhseGroupBin
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WhseGroupCode: Desc: WhseGroupCode   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param BinNum: Desc: BinNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.WhseGroupBinRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/WhseGroupBins(" + Company + "," + WhseGroupCode + "," + WarehouseCode + "," + BinNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_WhseGroupBins_Company_WhseGroupCode_WarehouseCode_BinNum(Company, WhseGroupCode, WarehouseCode, BinNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete WhseGroupBin item
   Description: Call UpdateExt to delete WhseGroupBin item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_WhseGroupBin
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WhseGroupCode: Desc: WhseGroupCode   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param BinNum: Desc: BinNum   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/WhseGroupBins(" + Company + "," + WhseGroupCode + "," + WarehouseCode + "," + BinNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_WhseGroupBinZones(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get WhseGroupBinZones items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_WhseGroupBinZones
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WhseGroupBinZoneRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/WhseGroupBinZones",headers=creds) as resp:
           return await resp.json()

async def post_WhseGroupBinZones(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_WhseGroupBinZones
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.WhseGroupBinZoneRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.WhseGroupBinZoneRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/WhseGroupBinZones", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_WhseGroupBinZones_Company_WhseGroupCode_WarehouseCode_ZoneID(Company, WhseGroupCode, WarehouseCode, ZoneID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the WhseGroupBinZone item
   Description: Calls GetByID to retrieve the WhseGroupBinZone item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WhseGroupBinZone
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WhseGroupCode: Desc: WhseGroupCode   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param ZoneID: Desc: ZoneID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.WhseGroupBinZoneRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/WhseGroupBinZones(" + Company + "," + WhseGroupCode + "," + WarehouseCode + "," + ZoneID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_WhseGroupBinZones_Company_WhseGroupCode_WarehouseCode_ZoneID(Company, WhseGroupCode, WarehouseCode, ZoneID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update WhseGroupBinZone for the service
   Description: Calls UpdateExt to update WhseGroupBinZone. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_WhseGroupBinZone
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WhseGroupCode: Desc: WhseGroupCode   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param ZoneID: Desc: ZoneID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.WhseGroupBinZoneRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/WhseGroupBinZones(" + Company + "," + WhseGroupCode + "," + WarehouseCode + "," + ZoneID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_WhseGroupBinZones_Company_WhseGroupCode_WarehouseCode_ZoneID(Company, WhseGroupCode, WarehouseCode, ZoneID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete WhseGroupBinZone item
   Description: Call UpdateExt to delete WhseGroupBinZone item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_WhseGroupBinZone
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WhseGroupCode: Desc: WhseGroupCode   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param ZoneID: Desc: ZoneID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/WhseGroupBinZones(" + Company + "," + WhseGroupCode + "," + WarehouseCode + "," + ZoneID + ")",headers=creds) as resp:
           return await resp.json()

async def get_WhseGroupItems(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get WhseGroupItems items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_WhseGroupItems
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WhseGroupItemRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/WhseGroupItems",headers=creds) as resp:
           return await resp.json()

async def post_WhseGroupItems(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_WhseGroupItems
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.WhseGroupItemRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.WhseGroupItemRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/WhseGroupItems", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_WhseGroupItems_Company_WhseGroupCode_WarehouseCode_ItemClass_ItemCode(Company, WhseGroupCode, WarehouseCode, ItemClass, ItemCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the WhseGroupItem item
   Description: Calls GetByID to retrieve the WhseGroupItem item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WhseGroupItem
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WhseGroupCode: Desc: WhseGroupCode   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param ItemClass: Desc: ItemClass   Required: True   Allow empty value : True
      :param ItemCode: Desc: ItemCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.WhseGroupItemRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/WhseGroupItems(" + Company + "," + WhseGroupCode + "," + WarehouseCode + "," + ItemClass + "," + ItemCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_WhseGroupItems_Company_WhseGroupCode_WarehouseCode_ItemClass_ItemCode(Company, WhseGroupCode, WarehouseCode, ItemClass, ItemCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update WhseGroupItem for the service
   Description: Calls UpdateExt to update WhseGroupItem. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_WhseGroupItem
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WhseGroupCode: Desc: WhseGroupCode   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param ItemClass: Desc: ItemClass   Required: True   Allow empty value : True
      :param ItemCode: Desc: ItemCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.WhseGroupItemRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/WhseGroupItems(" + Company + "," + WhseGroupCode + "," + WarehouseCode + "," + ItemClass + "," + ItemCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_WhseGroupItems_Company_WhseGroupCode_WarehouseCode_ItemClass_ItemCode(Company, WhseGroupCode, WarehouseCode, ItemClass, ItemCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete WhseGroupItem item
   Description: Call UpdateExt to delete WhseGroupItem item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_WhseGroupItem
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WhseGroupCode: Desc: WhseGroupCode   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param ItemClass: Desc: ItemClass   Required: True   Allow empty value : True
      :param ItemCode: Desc: ItemCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/WhseGroupItems(" + Company + "," + WhseGroupCode + "," + WarehouseCode + "," + ItemClass + "," + ItemCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_AvailEmployees(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get AvailEmployees items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AvailEmployees
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AvailEmployeesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/AvailEmployees",headers=creds) as resp:
           return await resp.json()

async def post_AvailEmployees(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AvailEmployees
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AvailEmployeesRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AvailEmployeesRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/AvailEmployees", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_AvailEmployees_Company_EmpID(Company, EmpID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AvailEmployee item
   Description: Calls GetByID to retrieve the AvailEmployee item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AvailEmployee
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AvailEmployeesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/AvailEmployees(" + Company + "," + EmpID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_AvailEmployees_Company_EmpID(Company, EmpID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update AvailEmployee for the service
   Description: Calls UpdateExt to update AvailEmployee. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AvailEmployee
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AvailEmployeesRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/AvailEmployees(" + Company + "," + EmpID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_AvailEmployees_Company_EmpID(Company, EmpID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete AvailEmployee item
   Description: Call UpdateExt to delete AvailEmployee item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AvailEmployee
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/AvailEmployees(" + Company + "," + EmpID + ")",headers=creds) as resp:
           return await resp.json()

async def get_AvailTransTypes(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get AvailTransTypes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AvailTransTypes
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AvailTransTypesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/AvailTransTypes",headers=creds) as resp:
           return await resp.json()

async def post_AvailTransTypes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AvailTransTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AvailTransTypesRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AvailTransTypesRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/AvailTransTypes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_AvailTransTypes_Company_WhseGroupCode_TransCode(Company, WhseGroupCode, TransCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AvailTransType item
   Description: Calls GetByID to retrieve the AvailTransType item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AvailTransType
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WhseGroupCode: Desc: WhseGroupCode   Required: True   Allow empty value : True
      :param TransCode: Desc: TransCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AvailTransTypesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/AvailTransTypes(" + Company + "," + WhseGroupCode + "," + TransCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_AvailTransTypes_Company_WhseGroupCode_TransCode(Company, WhseGroupCode, TransCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update AvailTransType for the service
   Description: Calls UpdateExt to update AvailTransType. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AvailTransType
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WhseGroupCode: Desc: WhseGroupCode   Required: True   Allow empty value : True
      :param TransCode: Desc: TransCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AvailTransTypesRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/AvailTransTypes(" + Company + "," + WhseGroupCode + "," + TransCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_AvailTransTypes_Company_WhseGroupCode_TransCode(Company, WhseGroupCode, TransCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete AvailTransType item
   Description: Call UpdateExt to delete AvailTransType item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AvailTransType
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WhseGroupCode: Desc: WhseGroupCode   Required: True   Allow empty value : True
      :param TransCode: Desc: TransCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/AvailTransTypes(" + Company + "," + WhseGroupCode + "," + TransCode + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WhseGroupListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseWhseGroup, whereClauseWhseGroupAttr, whereClauseWhseGroupEmp, whereClauseWhseGroupTrans, whereClauseWhseGroupWhse, whereClauseWhseGroupBin, whereClauseWhseGroupBinZone, whereClauseWhseGroupItem, whereClauseAvailEmployees, whereClauseAvailTransTypes, pageSize, absolutePage, epicorHeaders = None):
   """  
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
   params += "whereClauseWhseGroup=" + whereClauseWhseGroup
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseWhseGroupAttr=" + whereClauseWhseGroupAttr
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseWhseGroupEmp=" + whereClauseWhseGroupEmp
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseWhseGroupTrans=" + whereClauseWhseGroupTrans
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseWhseGroupWhse=" + whereClauseWhseGroupWhse
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseWhseGroupBin=" + whereClauseWhseGroupBin
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseWhseGroupBinZone=" + whereClauseWhseGroupBinZone
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseWhseGroupItem=" + whereClauseWhseGroupItem
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseAvailEmployees=" + whereClauseAvailEmployees
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseAvailTransTypes=" + whereClauseAvailTransTypes
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(whseGroupCode, epicorHeaders = None):
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
   params += "whseGroupCode=" + whseGroupCode

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_CreateUpdateAvailItems(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateUpdateAvailItems
   Description: Creates or updates the records for WhseGroupItems according to what option was selected (Part, Group, or Class)
   OperationID: CreateUpdateAvailItems
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateUpdateAvailItems_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateUpdateAvailItems_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateUpdateWhseGrpTrans(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateUpdateWhseGrpTrans
   Description: Creates or updates the WhseGroupTrans records according to what is selected in the availTransTypes
   OperationID: CreateUpdateWhseGrpTrans
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateUpdateWhseGrpTrans_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateUpdateWhseGrpTrans_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAvailEmployees(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAvailEmployees
   Description: Returns the list of available employees not assigned to any Warehouse Group yet
   OperationID: GetAvailEmployees
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAvailEmployees_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailEmployees_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAvailTransTypes(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAvailTransTypes
   Description: Creates and Returns the list of available Transactions Types
   OperationID: GetAvailTransTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAvailTransTypes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailTransTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePriority(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePriority
   Description: Used to verify that Priority must be between the range of whole values 0 - 9
   OperationID: OnChangePriority
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePriority_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePriority_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   OperationID: GetCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewWhseGroup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewWhseGroup
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewWhseGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewWhseGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewWhseGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewWhseGroupAttr(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewWhseGroupAttr
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewWhseGroupAttr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewWhseGroupAttr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewWhseGroupAttr_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewWhseGroupEmp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewWhseGroupEmp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewWhseGroupEmp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewWhseGroupEmp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewWhseGroupEmp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewWhseGroupTrans(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewWhseGroupTrans
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewWhseGroupTrans
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewWhseGroupTrans_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewWhseGroupTrans_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewWhseGroupWhse(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewWhseGroupWhse
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewWhseGroupWhse
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewWhseGroupWhse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewWhseGroupWhse_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewWhseGroupBin(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewWhseGroupBin
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewWhseGroupBin
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewWhseGroupBin_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewWhseGroupBin_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewWhseGroupBinZone(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewWhseGroupBinZone
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewWhseGroupBinZone
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewWhseGroupBinZone_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewWhseGroupBinZone_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewWhseGroupItem(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewWhseGroupItem
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewWhseGroupItem
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewWhseGroupItem_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewWhseGroupItem_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WhseGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AvailEmployeesRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_AvailEmployeesRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AvailTransTypesRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_AvailTransTypesRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WhseGroupAttrRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_WhseGroupAttrRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WhseGroupBinRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_WhseGroupBinRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WhseGroupBinZoneRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_WhseGroupBinZoneRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WhseGroupEmpRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_WhseGroupEmpRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WhseGroupItemRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_WhseGroupItemRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WhseGroupListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_WhseGroupListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WhseGroupRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_WhseGroupRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WhseGroupTransRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_WhseGroupTransRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WhseGroupWhseRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_WhseGroupWhseRow] = obj["value"]
      pass

class Erp_Tablesets_AvailEmployeesRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.EmpID:str = obj["EmpID"]
      self.Name:str = obj["Name"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AvailTransTypesRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.WhseGroupCode:str = obj["WhseGroupCode"]
      self.TransCode:str = obj["TransCode"]
      self.Description:str = obj["Description"]
      self.TransPriority:int = obj["TransPriority"]
      self.Selected:bool = obj["Selected"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_WhseGroupAttrRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.WhseGroupCode:str = obj["WhseGroupCode"]
      """  Warehouse Group Identifier.  """  
      self.AttrCode:str = obj["AttrCode"]
      """  Descriptive code assigned by user which uniquely identifies an attribute master record.  This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_WhseGroupBinRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.WhseGroupCode:str = obj["WhseGroupCode"]
      """  Warehouse Group Identifier.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Unique identifier for this warehouse assigned by the user.  """  
      self.BinNum:str = obj["BinNum"]
      """  The user defined bin number within the warehouse.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_WhseGroupBinZoneRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.WhseGroupCode:str = obj["WhseGroupCode"]
      """  Warehouse Group Identifier.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Unique identifier for this warehouse assigned by the user.  """  
      self.ZoneID:str = obj["ZoneID"]
      """  ID that uniquely Identifies a Zone within a warehouse.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_WhseGroupEmpRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.WhseGroupCode:str = obj["WhseGroupCode"]
      """  Warehouse Group Identifier.  """  
      self.EmpID:str = obj["EmpID"]
      """  Employee ID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EmpName:str = obj["EmpName"]
      """  Employee Name  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_WhseGroupItemRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.WhseGroupCode:str = obj["WhseGroupCode"]
      """  Warehouse Group Identifier.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Unique identifier for this warehouse assigned by the user.  """  
      self.ItemClass:str = obj["ItemClass"]
      """  Warehouse Group Item Class.  Valid values:  Part, Type, Group, Class.  """  
      self.ItemCode:str = obj["ItemCode"]
      """  Warehouse Group Item Code.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ItemDesc:str = obj["ItemDesc"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_WhseGroupListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.WhseGroupCode:str = obj["WhseGroupCode"]
      """  Warehouse Group Identifier.  """  
      self.WhseGroupDesc:str = obj["WhseGroupDesc"]
      """  Warehouse Group Description.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_WhseGroupRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.WhseGroupCode:str = obj["WhseGroupCode"]
      """  Warehouse Group Identifier.  """  
      self.WhseGroupDesc:str = obj["WhseGroupDesc"]
      """  Warehouse Group Description.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_WhseGroupTransRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.WhseGroupCode:str = obj["WhseGroupCode"]
      """  Warehouse Group Identifier.  """  
      self.TransCode:str = obj["TransCode"]
      """  Warehouse Group Transaction.  """  
      self.TransPriority:int = obj["TransPriority"]
      """  Transaction Priority.  Valid values are 1-99.  1 is the highest priority.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_WhseGroupWhseRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.WhseGroupCode:str = obj["WhseGroupCode"]
      """  Warehouse Group Identifier.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Unique identifier for this warehouse assigned by the user.  """  
      self.TransPriority:int = obj["TransPriority"]
      """  Transaction Priority.  Valid values are 1,2,3,4,5,6,7,8,9.  1 is the highest priority.  """  
      self.ItemType:str = obj["ItemType"]
      """  Warehouse Group Item Class for this Warehouse.  Valid values:  Part, Group, Class.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.WhseGroupWhseDescDescription:str = obj["WhseGroupWhseDescDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CreateUpdateAvailItems_input:
   """ Required : 
   groupCode
   whseCode
   typeClass
   ds
   ds1
   """  
   def __init__(self, obj):
      self.groupCode:str = obj["groupCode"]
      """  Warehouse Group Code.  """  
      self.whseCode:str = obj["whseCode"]
      """  Warehouse Code.  """  
      self.typeClass:str = obj["typeClass"]
      """  Item Class.  """  
      self.ds:list[Erp_Tablesets_AvailItemsTableset] = obj["ds"]
      self.ds1:list[Erp_Tablesets_WhseGroupTableset] = obj["ds1"]
      pass

class CreateUpdateAvailItems_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AvailItemsTableset] = obj["ds"]
      self.ds1:list[Erp_Tablesets_WhseGroupTableset] = obj["ds1"]
      pass

      """  output parameters  """  

class CreateUpdateWhseGrpTrans_input:
   """ Required : 
   groupCode
   ds
   """  
   def __init__(self, obj):
      self.groupCode:str = obj["groupCode"]
      """  Warehouse Group Code.  """  
      self.ds:list[Erp_Tablesets_WhseGroupTableset] = obj["ds"]
      pass

class CreateUpdateWhseGrpTrans_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_WhseGroupTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   whseGroupCode
   """  
   def __init__(self, obj):
      self.whseGroupCode:str = obj["whseGroupCode"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_AvailEmployeesRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.EmpID:str = obj["EmpID"]
      self.Name:str = obj["Name"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AvailItemsRow:
   def __init__(self, obj):
      self.ClassID:str = obj["ClassID"]
      self.Company:str = obj["Company"]
      self.PartNum:str = obj["PartNum"]
      self.ProdCode:str = obj["ProdCode"]
      self.PartDescription:str = obj["PartDescription"]
      self.Description:str = obj["Description"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AvailItemsTableset:
   def __init__(self, obj):
      self.AvailItems:list[Erp_Tablesets_AvailItemsRow] = obj["AvailItems"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_AvailTransTypesRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.WhseGroupCode:str = obj["WhseGroupCode"]
      self.TransCode:str = obj["TransCode"]
      self.Description:str = obj["Description"]
      self.TransPriority:int = obj["TransPriority"]
      self.Selected:bool = obj["Selected"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtWhseGroupTableset:
   def __init__(self, obj):
      self.WhseGroup:list[Erp_Tablesets_WhseGroupRow] = obj["WhseGroup"]
      self.WhseGroupAttr:list[Erp_Tablesets_WhseGroupAttrRow] = obj["WhseGroupAttr"]
      self.WhseGroupEmp:list[Erp_Tablesets_WhseGroupEmpRow] = obj["WhseGroupEmp"]
      self.WhseGroupTrans:list[Erp_Tablesets_WhseGroupTransRow] = obj["WhseGroupTrans"]
      self.WhseGroupWhse:list[Erp_Tablesets_WhseGroupWhseRow] = obj["WhseGroupWhse"]
      self.WhseGroupBin:list[Erp_Tablesets_WhseGroupBinRow] = obj["WhseGroupBin"]
      self.WhseGroupBinZone:list[Erp_Tablesets_WhseGroupBinZoneRow] = obj["WhseGroupBinZone"]
      self.WhseGroupItem:list[Erp_Tablesets_WhseGroupItemRow] = obj["WhseGroupItem"]
      self.AvailEmployees:list[Erp_Tablesets_AvailEmployeesRow] = obj["AvailEmployees"]
      self.AvailTransTypes:list[Erp_Tablesets_AvailTransTypesRow] = obj["AvailTransTypes"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_WhseGroupAttrRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.WhseGroupCode:str = obj["WhseGroupCode"]
      """  Warehouse Group Identifier.  """  
      self.AttrCode:str = obj["AttrCode"]
      """  Descriptive code assigned by user which uniquely identifies an attribute master record.  This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_WhseGroupBinRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.WhseGroupCode:str = obj["WhseGroupCode"]
      """  Warehouse Group Identifier.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Unique identifier for this warehouse assigned by the user.  """  
      self.BinNum:str = obj["BinNum"]
      """  The user defined bin number within the warehouse.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_WhseGroupBinZoneRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.WhseGroupCode:str = obj["WhseGroupCode"]
      """  Warehouse Group Identifier.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Unique identifier for this warehouse assigned by the user.  """  
      self.ZoneID:str = obj["ZoneID"]
      """  ID that uniquely Identifies a Zone within a warehouse.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_WhseGroupEmpRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.WhseGroupCode:str = obj["WhseGroupCode"]
      """  Warehouse Group Identifier.  """  
      self.EmpID:str = obj["EmpID"]
      """  Employee ID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EmpName:str = obj["EmpName"]
      """  Employee Name  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_WhseGroupItemRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.WhseGroupCode:str = obj["WhseGroupCode"]
      """  Warehouse Group Identifier.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Unique identifier for this warehouse assigned by the user.  """  
      self.ItemClass:str = obj["ItemClass"]
      """  Warehouse Group Item Class.  Valid values:  Part, Type, Group, Class.  """  
      self.ItemCode:str = obj["ItemCode"]
      """  Warehouse Group Item Code.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ItemDesc:str = obj["ItemDesc"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_WhseGroupListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.WhseGroupCode:str = obj["WhseGroupCode"]
      """  Warehouse Group Identifier.  """  
      self.WhseGroupDesc:str = obj["WhseGroupDesc"]
      """  Warehouse Group Description.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_WhseGroupListTableset:
   def __init__(self, obj):
      self.WhseGroupList:list[Erp_Tablesets_WhseGroupListRow] = obj["WhseGroupList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_WhseGroupRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.WhseGroupCode:str = obj["WhseGroupCode"]
      """  Warehouse Group Identifier.  """  
      self.WhseGroupDesc:str = obj["WhseGroupDesc"]
      """  Warehouse Group Description.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_WhseGroupTableset:
   def __init__(self, obj):
      self.WhseGroup:list[Erp_Tablesets_WhseGroupRow] = obj["WhseGroup"]
      self.WhseGroupAttr:list[Erp_Tablesets_WhseGroupAttrRow] = obj["WhseGroupAttr"]
      self.WhseGroupEmp:list[Erp_Tablesets_WhseGroupEmpRow] = obj["WhseGroupEmp"]
      self.WhseGroupTrans:list[Erp_Tablesets_WhseGroupTransRow] = obj["WhseGroupTrans"]
      self.WhseGroupWhse:list[Erp_Tablesets_WhseGroupWhseRow] = obj["WhseGroupWhse"]
      self.WhseGroupBin:list[Erp_Tablesets_WhseGroupBinRow] = obj["WhseGroupBin"]
      self.WhseGroupBinZone:list[Erp_Tablesets_WhseGroupBinZoneRow] = obj["WhseGroupBinZone"]
      self.WhseGroupItem:list[Erp_Tablesets_WhseGroupItemRow] = obj["WhseGroupItem"]
      self.AvailEmployees:list[Erp_Tablesets_AvailEmployeesRow] = obj["AvailEmployees"]
      self.AvailTransTypes:list[Erp_Tablesets_AvailTransTypesRow] = obj["AvailTransTypes"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_WhseGroupTransRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.WhseGroupCode:str = obj["WhseGroupCode"]
      """  Warehouse Group Identifier.  """  
      self.TransCode:str = obj["TransCode"]
      """  Warehouse Group Transaction.  """  
      self.TransPriority:int = obj["TransPriority"]
      """  Transaction Priority.  Valid values are 1-99.  1 is the highest priority.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_WhseGroupWhseRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.WhseGroupCode:str = obj["WhseGroupCode"]
      """  Warehouse Group Identifier.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Unique identifier for this warehouse assigned by the user.  """  
      self.TransPriority:int = obj["TransPriority"]
      """  Transaction Priority.  Valid values are 1,2,3,4,5,6,7,8,9.  1 is the highest priority.  """  
      self.ItemType:str = obj["ItemType"]
      """  Warehouse Group Item Class for this Warehouse.  Valid values:  Part, Group, Class.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.WhseGroupWhseDescDescription:str = obj["WhseGroupWhseDescDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class GetAvailEmployees_input:
   """ Required : 
   groupCode
   """  
   def __init__(self, obj):
      self.groupCode:str = obj["groupCode"]
      """  Warehouse Group Code.  """  
      pass

class GetAvailEmployees_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_WhseGroupTableset] = obj["returnObj"]
      pass

class GetAvailTransTypes_input:
   """ Required : 
   groupCode
   """  
   def __init__(self, obj):
      self.groupCode:str = obj["groupCode"]
      """  Warehouse Group Code.  """  
      pass

class GetAvailTransTypes_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_WhseGroupTableset] = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   whseGroupCode
   """  
   def __init__(self, obj):
      self.whseGroupCode:str = obj["whseGroupCode"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_WhseGroupTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_WhseGroupTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_WhseGroupTableset] = obj["returnObj"]
      pass

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      self.fieldName:str = obj["fieldName"]
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_WhseGroupListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewWhseGroupAttr_input:
   """ Required : 
   ds
   whseGroupCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_WhseGroupTableset] = obj["ds"]
      self.whseGroupCode:str = obj["whseGroupCode"]
      pass

class GetNewWhseGroupAttr_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_WhseGroupTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewWhseGroupBinZone_input:
   """ Required : 
   ds
   whseGroupCode
   warehouseCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_WhseGroupTableset] = obj["ds"]
      self.whseGroupCode:str = obj["whseGroupCode"]
      self.warehouseCode:str = obj["warehouseCode"]
      pass

class GetNewWhseGroupBinZone_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_WhseGroupTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewWhseGroupBin_input:
   """ Required : 
   ds
   whseGroupCode
   warehouseCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_WhseGroupTableset] = obj["ds"]
      self.whseGroupCode:str = obj["whseGroupCode"]
      self.warehouseCode:str = obj["warehouseCode"]
      pass

class GetNewWhseGroupBin_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_WhseGroupTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewWhseGroupEmp_input:
   """ Required : 
   ds
   whseGroupCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_WhseGroupTableset] = obj["ds"]
      self.whseGroupCode:str = obj["whseGroupCode"]
      pass

class GetNewWhseGroupEmp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_WhseGroupTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewWhseGroupItem_input:
   """ Required : 
   ds
   whseGroupCode
   warehouseCode
   itemClass
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_WhseGroupTableset] = obj["ds"]
      self.whseGroupCode:str = obj["whseGroupCode"]
      self.warehouseCode:str = obj["warehouseCode"]
      self.itemClass:str = obj["itemClass"]
      pass

class GetNewWhseGroupItem_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_WhseGroupTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewWhseGroupTrans_input:
   """ Required : 
   ds
   whseGroupCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_WhseGroupTableset] = obj["ds"]
      self.whseGroupCode:str = obj["whseGroupCode"]
      pass

class GetNewWhseGroupTrans_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_WhseGroupTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewWhseGroupWhse_input:
   """ Required : 
   ds
   whseGroupCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_WhseGroupTableset] = obj["ds"]
      self.whseGroupCode:str = obj["whseGroupCode"]
      pass

class GetNewWhseGroupWhse_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_WhseGroupTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewWhseGroup_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_WhseGroupTableset] = obj["ds"]
      pass

class GetNewWhseGroup_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_WhseGroupTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseWhseGroup
   whereClauseWhseGroupAttr
   whereClauseWhseGroupEmp
   whereClauseWhseGroupTrans
   whereClauseWhseGroupWhse
   whereClauseWhseGroupBin
   whereClauseWhseGroupBinZone
   whereClauseWhseGroupItem
   whereClauseAvailEmployees
   whereClauseAvailTransTypes
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseWhseGroup:str = obj["whereClauseWhseGroup"]
      self.whereClauseWhseGroupAttr:str = obj["whereClauseWhseGroupAttr"]
      self.whereClauseWhseGroupEmp:str = obj["whereClauseWhseGroupEmp"]
      self.whereClauseWhseGroupTrans:str = obj["whereClauseWhseGroupTrans"]
      self.whereClauseWhseGroupWhse:str = obj["whereClauseWhseGroupWhse"]
      self.whereClauseWhseGroupBin:str = obj["whereClauseWhseGroupBin"]
      self.whereClauseWhseGroupBinZone:str = obj["whereClauseWhseGroupBinZone"]
      self.whereClauseWhseGroupItem:str = obj["whereClauseWhseGroupItem"]
      self.whereClauseAvailEmployees:str = obj["whereClauseAvailEmployees"]
      self.whereClauseAvailTransTypes:str = obj["whereClauseAvailTransTypes"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_WhseGroupTableset] = obj["returnObj"]
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

class OnChangePriority_input:
   """ Required : 
   priority
   """  
   def __init__(self, obj):
      self.priority:int = obj["priority"]
      """  Priority.  """  
      pass

class OnChangePriority_output:
   def __init__(self, obj):
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtWhseGroupTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtWhseGroupTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_WhseGroupTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_WhseGroupTableset] = obj["ds"]
      pass

      """  output parameters  """  

